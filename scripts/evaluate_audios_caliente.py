"""
Mide la latencia de speech-emotion dentro de UN solo proceso de Python.

- Llamada 1: incluye la carga del modelo (frío).
- Llamadas 2..N: si el toolkit guarda el modelo en memoria, son en caliente.

Uso:
    uv run python src/medir_caliente.py src/audios --repeticiones 5
"""
import os
import sys
import time
import argparse
from pathlib import Path
from statistics import mean, median

os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")

try:
    from speech_emotion import predict_emotion
except ImportError:
    from speech_emotion.inference import predict_emotion

ap = argparse.ArgumentParser()
ap.add_argument("ruta", help="carpeta con .wav o un archivo .wav")
ap.add_argument("--repeticiones", type=int, default=5, help="veces que se repite el primer audio")
ap.add_argument("--device", default="cpu")
ap.add_argument("--model-config", default=str(Path(__file__).resolve().parent / "model.json"))
args = ap.parse_args()

ruta = Path(args.ruta)
audios = sorted(ruta.rglob("*.wav")) if ruta.is_dir() else [ruta]
if not audios:
    sys.exit("No se encontraron archivos .wav")


def medir(audio):
    t0 = time.perf_counter()
    predict_emotion(audio_path=str(audio), language="es", mode="audio",
                    device=args.device, model_config_path=args.model_config)
    return time.perf_counter() - t0


# 1) Mismo audio repetido: revela si el toolkit recarga el modelo en cada llamada
print(f"Repitiendo {audios[0].name} {args.repeticiones} veces:")
reps = [medir(audios[0]) for _ in range(args.repeticiones)]
for i, t in enumerate(reps, 1):
    print(f"  llamada {i}: {t:7.3f} s" + ("   <- incluye carga del modelo" if i == 1 else ""))

if len(reps) > 1:
    resto = mean(reps[1:])
    if resto > 0.6 * reps[0]:
        print("\nDIAGNÓSTICO: las llamadas siguientes tardan casi lo mismo que la primera.\n"
              "El toolkit RECARGA el modelo en cada llamada: estos tiempos NO son en caliente.")
    else:
        print(f"\nDIAGNÓSTICO: el modelo queda en memoria. Carga ≈ {reps[0] - resto:.2f} s, "
              f"inferencia en caliente ≈ {resto:.3f} s")

# 2) Todos los audios, ya con el modelo cargado
tiempos = [medir(a) for a in audios]
print(f"\nAudios procesados: {len(tiempos)}")
print(f"Tiempo total:      {sum(tiempos):.3f} s")
print(f"Tiempo promedio:   {mean(tiempos):.3f} s")
print(f"Mediana:           {median(tiempos):.3f} s")
print(f"Mínimo / máximo:   {min(tiempos):.3f} / {max(tiempos):.3f} s")
