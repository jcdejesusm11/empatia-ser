# from transformers import pipeline
# import time
# import numpy as np


# classifier = pipeline(
#     "audio-classification",
#     model="UMUTeam/w2v-bert-emotion-es"
# )

# tiempos = []
# predicciones = []
# for _ in range(15):
#     inicio = time.perf_counter()
#     prediction = classifier("./audios/enojo-banco-occidente-usuario-turno-002.wav")
#     fin = time.perf_counter()
#     predicciones.append(prediction[0])
#     tiempos.append(fin - inicio) 
    
# tiempo_promedio = np.average(tiempos)

# print(predicciones)
# print("")
# print(f"Tiempo promedio: {tiempo_promedio}")
# print("")
# print(tiempos)

import torch
import librosa
import logging
from transformers import logging as transformers_logging, SeamlessM4TFeatureExtractor, AutoModelForAudioClassification

transformers_logging.set_verbosity_error()
logging.getLogger("transformers").setLevel(logging.ERROR)

# 1. Configurar el FeatureExtractor nativo de la arquitectura BERT de audio
feature_extractor = SeamlessM4TFeatureExtractor.from_pretrained("UMUTeam/w2v-bert-emotion-es")

# 2. CARGA RECOMENDADA: Aseguramos semillas globales por estabilidad de hardware
torch.manual_seed(42)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(42)

# Cargamos el modelo forzando el código remoto nativo
model = AutoModelForAudioClassification.from_pretrained(
    "UMUTeam/w2v-bert-emotion-es", 
    trust_remote_code=True
)

# Configurar dispositivo (GPU/CPU) y congelar pesos en modo evaluación
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
model.eval() # Congela el dropout de forma estricta para evitar variaciones

def categorizar_llamada_ajustada(predicciones):
    # Al estar ordenada de mayor a menor, la primera es la emoción dominante
    dominante = predicciones[0]
    emocion = dominante["label"]
    score = dominante["score"]
    
    # Mapeo estricto basado en la naturaleza de la emoción ganadora
    if emocion in ["joy", "neutral"]:
        return {
            "categoria": "LOW",
            "detalle": f"Tono predominante: {emocion.upper()} ({round(score*100, 2)}%). El agente sigue el flujo estándar."
        }
        
    elif emocion == "disgust":
        return {
            "categoria": "MEDIUM",
            "detalle": f"Frustración detectada: {emocion.upper()} ({round(score*100, 2)}%). El agente debe adaptar empatía."
        }
        
    elif emocion in ["anger", "fear", "sadness"]:
        if score < 0.20:
            return {
                "categoria": "MEDIUM",
                "detalle": f"Insatisfacción leve (Emoción: {emocion.upper()} con {round(score*100, 2)}%). Monitorear tono."
            }
        else:
            return {
                "categoria": "HIGH",
                "detalle": f"Escalación emocional crítica: {emocion.upper()} ({round(score*100, 2)}%). Activar protocolo de retención."
            }

# 3. Función clasificadora corregida y simplificada
def classifier(audio_path):
    # 1. Cargar y remuestrear a 16kHz
    speech, sample_rate = librosa.load(audio_path, sr=16000)
    
    # 2. Extraer características para W2V-BERT
    inputs = feature_extractor(speech, sampling_rate=16000, return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}
    
    # 3. Inferencia síncrona fija
    with torch.no_grad():
        outputs = model(**inputs)
    
    # 4. Extraer logits controlando las propiedades dinámicas del modelo
    if hasattr(outputs, "logits"):
        logits = outputs.logits
    elif isinstance(outputs, dict) and "logits" in outputs:
        logits = outputs["logits"]
    else:
        logits = outputs
        
    # 5. Calcular probabilidades con Softmax extrayendo el primer elemento del batch [0]
    probs = torch.nn.functional.softmax(logits, dim=-1)[0]
    
    # 6. Mapear cada probabilidad con su respectivo nombre de emoción
    all_predictions = []
    for label_id, prob in enumerate(probs):
        # CORRECCIÓN: label_id ya es un int normal de Python, eliminamos .item()
        label_name = model.config.id2label[label_id]
        all_predictions.append({
            "label": label_name,
            "score": round(prob.item(), 4)
        })
    
    # 7. Ordenar la lista de mayor a menor probabilidad
    all_predictions = sorted(all_predictions, key=lambda x: x["score"], reverse=True)
    
    print(all_predictions)
    return all_predictions

# Ejecución de prueba
print(categorizar_llamada_ajustada(classifier(audio_path="./audios/frustracion/impaciente-2-banco-occidente-usuario-turno-4.wav")))