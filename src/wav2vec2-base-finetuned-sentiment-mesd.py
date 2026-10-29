"""
Evaluación de somosnlp-hackathon-2022/wav2vec2-base-finetuned-sentiment-mesd
sobre carpetas de audios (.wav), con Sentiment Score (0-100), Sentimiento (-1 a 1)
y latencia en caliente por fragmento.
 
Uso:
    uv run python src/wav2vec2-sentiment-mesd.py src/audios --online        # 1a vez (descarga)
    uv run python src/wav2vec2-sentiment-mesd.py src/audios                 # offline
    uv run python src/wav2vec2-sentiment-mesd.py src/audios --ventana 4     # fragmentos de 4 s
    uv run python src/wav2vec2-sentiment-mesd.py src/audios --salida mesd.json
"""
import os
import sys
import json
import time
import argparse
from pathlib import Path
from statistics import mean, median
from collections import Counter, defaultdict
 
MODEL_ID = "somosnlp-hackathon-2022/wav2vec2-base-finetuned-sentiment-mesd"
BASE_ID = "facebook/wav2vec2-base"  # modelo base (feature extractor de respaldo)
SR = 16000
 
# ---------------------------------------------------------------------------
# Normalización de etiquetas (el model card no documenta los nombres exactos)
# ---------------------------------------------------------------------------
ALIAS = {
    "anger": "anger", "angry": "anger", "enojo": "anger", "ira": "anger",
    "disgust": "disgust", "asco": "disgust",
    "fear": "fear", "miedo": "fear",
    "happiness": "joy", "happy": "joy", "joy": "joy",
    "alegria": "joy", "alegría": "joy", "felicidad": "joy",
    "neutral": "neutral",
    "sadness": "sadness", "sad": "sadness", "tristeza": "sadness",
    "surprise": "surprise", "sorpresa": "surprise",
}
 
# Riesgo para el Sentiment Score (0-100) y valencia para el Sentimiento (-1 a 1)
RIESGO = {"joy": 0.00, "neutral": 0.20, "surprise": 0.40, "sadness": 0.55,
          "disgust": 0.60, "fear": 0.75, "anger": 0.95}
VALENCIA = {"joy": 1.0, "neutral": 0.0, "surprise": 0.0, "sadness": -0.6,
            "fear": -0.6, "disgust": -0.7, "anger": -1.0}
UMBRAL_MEDIUM, UMBRAL_HIGH = 40.0, 70.0
EXCESO_MINIMO = 0.05  # masa mínima sobre el azar para considerar que hay señal
OBJETIVO_MS = 200.0
 
 
def normalizar(label):
    return ALIAS.get(str(label).strip().lower(), str(label).strip().lower())
 
 
def puntuar(predicciones):
    """
    Método con piso de ruido: solo cuenta la probabilidad que cada emoción tiene
    por encima del azar (1/n). Devuelve dict con SS, sentimiento y categoría.
    """
    piso = 1.0 / len(predicciones)
    exceso = [(p["label"], max(p["score"] - piso, 0.0)) for p in predicciones]
    total = sum(e for _, e in exceso)
    dominante = max(predicciones, key=lambda p: p["score"])
    base = {"emocion_dominante": dominante["label"],
            "confianza": round(dominante["score"] * 100, 2)}
    if total < EXCESO_MINIMO:
        return {**base, "sentiment_score": None, "sentimiento": None, "categoria": "UNCERTAIN"}
 
    ss = 100 * sum(e * RIESGO.get(l, 0.5) for l, e in exceso) / total
    sent = sum(e * VALENCIA.get(l, 0.0) for l, e in exceso) / total
    cat = "LOW" if ss < UMBRAL_MEDIUM else "MEDIUM" if ss < UMBRAL_HIGH else "HIGH"
    return {**base, "sentiment_score": round(ss, 2), "sentimiento": round(sent, 3), "categoria": cat}
 
 
def fragmentar(x, segundos, minimo=2.0):
    """Divide el audio en fragmentos consecutivos; descarta un resto final < `minimo` s."""
    if not segundos:
        return [x]
    n = int(segundos * SR)
    if len(x) <= n:
        return [x]
    trozos = [x[i:i + n] for i in range(0, len(x), n)]
    if len(trozos[-1]) < minimo * SR:
        trozos = trozos[:-1]
    return trozos
 
 
def percentil(valores, q):
    v = sorted(valores)
    k = (len(v) - 1) * q
    i = int(k)
    return v[i] if i + 1 >= len(v) else v[i] + (v[i + 1] - v[i]) * (k - i)
 
 
# ---------------------------------------------------------------------------
# Modelo
# ---------------------------------------------------------------------------
def cargar_modelo(device, hilos):
    import torch
    from transformers import AutoFeatureExtractor, AutoModelForAudioClassification
 
    if hilos:
        torch.set_num_threads(hilos)
 
    offline = os.environ.get("HF_HUB_OFFLINE") == "1"
    sugerencia = ("\nEstá en modo offline y el archivo no está en la caché local. "
                  "Ejecute una vez con --online para descargarlo." if offline else "")
 
    # Algunos modelos del hackathon 2022 no incluyen preprocessor_config.json;
    # en ese caso se usa el del modelo base con el que fueron entrenados.
    try:
        fe = AutoFeatureExtractor.from_pretrained(MODEL_ID)
    except OSError:
        from transformers import Wav2Vec2FeatureExtractor
        try:
            fe = Wav2Vec2FeatureExtractor.from_pretrained(BASE_ID)
            print(f"AVISO: {MODEL_ID} no trae preprocessor_config.json; "
                  f"se usa el feature extractor de {BASE_ID}.")
        except OSError as e:
            sys.exit(f"ERROR: no se pudo cargar el feature extractor ({e}).{sugerencia}")
 
    try:
        model, info = AutoModelForAudioClassification.from_pretrained(MODEL_ID, output_loading_info=True)
    except OSError as e:
        sys.exit(f"ERROR: no se pudo cargar el modelo ({e}).{sugerencia}")
 
    # Lección de UMUTeam: si falta la cabeza, el modelo clasifica con pesos aleatorios
    faltantes = [k for k in info.get("missing_keys", []) if "classifier" in k or "projector" in k]
    if faltantes:
        sys.exit(f"ERROR: la cabeza de clasificación no se cargó del checkpoint: {faltantes}\n"
                 "Las predicciones serían aleatorias. No se continúa.")
 
    model.to(device).eval()
    etiquetas = {i: normalizar(l) for i, l in model.config.id2label.items()}
    print(f"Modelo: {MODEL_ID}")
    print(f"Parámetros: {sum(p.numel() for p in model.parameters()):,} | dispositivo: {device} "
          f"| hilos CPU: {torch.get_num_threads()}")
    print(f"Etiquetas del modelo: {model.config.id2label}")
    print(f"Etiquetas normalizadas: {etiquetas}")
    genericas = [l for l in etiquetas.values() if l.startswith("label_")]
    if genericas:
        print("AVISO: el modelo usa etiquetas genéricas (LABEL_n); el mapeo a emociones "
              "no es posible sin conocer su significado.")
    sin_peso = [l for l in etiquetas.values() if l not in RIESGO]
    if sin_peso:
        print(f"AVISO: etiquetas sin peso definido (se usará un valor por defecto): {sin_peso}")
    return torch, fe, model, etiquetas
 
 
def inferir(torch, fe, model, etiquetas, x, device):
    """Devuelve (predicciones ordenadas, ms_caracteristicas, ms_modelo)."""
    t0 = time.perf_counter()
    inputs = fe(x, sampling_rate=SR, return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}
    t1 = time.perf_counter()
    with torch.inference_mode():
        logits = model(**inputs).logits
    if device.startswith("cuda"):
        torch.cuda.synchronize()
    t2 = time.perf_counter()
    probs = torch.softmax(logits, dim=-1)[0].tolist()
    preds = sorted(({"label": etiquetas[i], "score": p} for i, p in enumerate(probs)),
                   key=lambda p: p["score"], reverse=True)
    return preds, (t1 - t0) * 1000, (t2 - t1) * 1000
 
 
# ---------------------------------------------------------------------------
# Ejecución
# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=f"Evaluación de {MODEL_ID}")
    ap.add_argument("rutas", nargs="+", help="archivos .wav o carpetas")
    ap.add_argument("--device", default="cpu", help="cpu, cuda o cuda:0")
    ap.add_argument("--hilos", type=int, help="hilos de CPU para PyTorch")
    ap.add_argument("--ventana", type=float, help="fragmentar cada audio en trozos de N segundos")
    ap.add_argument("--trim", action="store_true", help="recortar silencios de inicio y fin")
    ap.add_argument("--online", action="store_true", help="permitir descargas de Hugging Face")
    ap.add_argument("--salida", help="guardar resultados en JSON")
    args = ap.parse_args()
 
    # Debe definirse antes de importar transformers
    os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")
    os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")
    if not args.online:
        os.environ["HF_HUB_OFFLINE"] = "1"
        os.environ["TRANSFORMERS_OFFLINE"] = "1"
 
    import librosa
 
    audios = []
    for r in args.rutas:
        p = Path(r)
        audios += sorted(p.rglob("*.wav")) if p.is_dir() else ([p] if p.is_file() else [])
    if not audios:
        sys.exit("No se encontraron archivos .wav.")
 
    torch, fe, model, etiquetas = cargar_modelo(args.device, args.hilos)
 
    # Calentamiento: la primera inferencia incluye inicializaciones internas de PyTorch
    import numpy as np
    for _ in range(2):
        inferir(torch, fe, model, etiquetas, np.zeros(SR * 4, dtype=np.float32), args.device)
 
    print(f"\n{'audio':55s} {'dur':>5s} {'emoción':8s} {'conf':>6s} {'SS':>6s} "
          f"{'sent':>6s} {'categoría':9s} {'ms/frag':>8s}")
    resultados, lat_frag, lat_feat, lat_model = [], [], [], []
    resumen_cat, resumen_emo = defaultdict(Counter), defaultdict(Counter)
 
    for audio in audios:
        try:
            x, _ = librosa.load(str(audio), sr=SR, mono=True)
        except Exception as e:
            print(f"ERROR leyendo {audio}: {e}", file=sys.stderr)
            continue
        if args.trim:
            x, _ = librosa.effects.trim(x, top_db=30)
 
        fragmentos = []
        for trozo in fragmentar(x, args.ventana):
            preds, ms_f, ms_m = inferir(torch, fe, model, etiquetas, trozo, args.device)
            lat_feat.append(ms_f)
            lat_model.append(ms_m)
            lat_frag.append(ms_f + ms_m)
            fragmentos.append({"duracion_s": round(len(trozo) / SR, 2), "ms": round(ms_f + ms_m, 1),
                               "scores": {p["label"]: p["score"] for p in preds}, **puntuar(preds)})
 
        # Resultado del audio: el fragmento con mayor riesgo (un pico no se diluye)
        validos = [f for f in fragmentos if f["sentiment_score"] is not None]
        final = max(validos, key=lambda f: f["sentiment_score"]) if validos else fragmentos[0]
        ms_prom = mean(f["ms"] for f in fragmentos)
 
        carpeta = audio.parent.name
        resumen_cat[carpeta][final["categoria"]] += 1
        resumen_emo[carpeta][final["emocion_dominante"]] += 1
        resultados.append({"audio": str(audio), "duracion_s": round(len(x) / SR, 2),
                           "resultado": final, "fragmentos": fragmentos})
 
        ss = "  -  " if final["sentiment_score"] is None else f"{final['sentiment_score']:6.1f}"
        sent = "  -  " if final["sentimiento"] is None else f"{final['sentimiento']:+6.2f}"
        print(f"{carpeta + '/' + audio.name:55s} {len(x) / SR:5.1f} {final['emocion_dominante']:8s} "
              f"{final['confianza']:5.1f}% {ss} {sent} {final['categoria']:9s} {ms_prom:8.1f}")
 
    if not lat_frag:
        sys.exit("No se procesó ningún audio.")
 
    # -------------------- Resumen --------------------
    print("\nResumen por carpeta (categoría del Sentiment Score):")
    for carpeta in sorted(resumen_cat):
        total = sum(resumen_cat[carpeta].values())
        cats = ", ".join(f"{c} {n} ({100 * n / total:.0f}%)" for c, n in sorted(resumen_cat[carpeta].items()))
        emos = ", ".join(f"{e} {n}" for e, n in resumen_emo[carpeta].most_common())
        print(f"  {carpeta:15s} {total:3d} audios -> {cats}")
        print(f"  {'':15s} emociones: {emos}")
 
    bajo = sum(t < OBJETIVO_MS for t in lat_frag)
    print(f"\nLatencia en caliente por fragmento ({len(lat_frag)} fragmentos"
          f"{f', ventana {args.ventana:g} s' if args.ventana else ', audio completo'}):")
    print(f"  promedio: {mean(lat_frag):8.1f} ms   (características {mean(lat_feat):.1f} ms + "
          f"modelo {mean(lat_model):.1f} ms)")
    print(f"  mediana:  {median(lat_frag):8.1f} ms")
    print(f"  p95:      {percentil(lat_frag, 0.95):8.1f} ms")
    print(f"  mín/máx:  {min(lat_frag):8.1f} / {max(lat_frag):.1f} ms")
    print(f"  < {OBJETIVO_MS:.0f} ms: {bajo}/{len(lat_frag)} ({100 * bajo / len(lat_frag):.0f}%)")
 
    if args.salida:
        Path(args.salida).write_text(json.dumps(resultados, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nResultados guardados en {args.salida}")
 
 
if __name__ == "__main__":
    main()