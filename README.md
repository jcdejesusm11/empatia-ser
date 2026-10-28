# EmpaIA - SPEECH EMOTION RECOGNITION

### Disclaimer 
_THIS IS AN EXPERIMENTAL REPOSITORY. 
THESE PRE-TRAINED ALGORITHMS DO NOT ENSURE A 100% ACCURACY IN SPEECH EMOTION RECOGNITION
AND MOST OF THEM WOULD RETURN FALSE POSITIVES OR NEGATIVES IN SOME DEGREE.
THE GOAL OF THIS REPO IS TO IDENTIFY AND TEST PRE-TRAINED MODELS FROM HUGGING FACE
AS PART OF THE ARCHITECTURAL DESIGN OF EMPATIA_


### Benchmarking

#### Dataset
Basado en los audios/transcripciones generados en entornos productivos, se generaron set de audios de acuerdo
a las caracteristicas de entonación de los usuarios y a la escala de análisis de sentimiento existente (neutral, frustración, otro).
Los dataset cumple con las siguientes caracteristicas para poder evaluar la precision de los modelos de acuerdo a los requisitos
funcionales y no funcionales del analisis de sentimiento de empatia:

- Duración entre 2 segundos y 16 segundos.
- Tamaño de 20 audios por escala (muestra pequeña debido al margén de tiempo y limitaciones de los recursos).
- Formato .wav

**Modelo UMUTeam/w2v-bert-emotion-es** 
- Descripción: modelo de clasificación de audio (SER) en español basado en wav2vec2-bert, etiquetado para reconocimiento de emociones.
- Autor(es): UMUTeam - Universidad de Murcia.
- Repositorio de modelo: https://github.com/NLP-UMUTeam/umuteam-speech-emotion
- Entorno de ejecución: **local**
- Resultados:

## Frustration folder (`audios/frustracion/`)

**Expected category:** MEDIUM · **Correct:** 13/20 (65%) · **Missed (LOW):** 7/20 (35%)

| Audio | Top emotion | Confidence | SS | Category | Correct |
|---|---|---:|---:|---|:---:|
| usuario-1 | disgust | 99.7% | 60.0 | MEDIUM | ✅ |
| usuario-2 | neutral | 99.5% | 20.0 | LOW | ❌ |
| usuario-3 | neutral | 98.5% | 20.0 | LOW | ❌ |
| usuario-4 | disgust | 99.8% | 60.0 | MEDIUM | ✅ |
| usuario-5 | disgust | 92.1% | 60.0 | MEDIUM | ✅ |
| usuario-6 | neutral | 99.5% | 20.0 | LOW | ❌ |
| usuario-7 | neutral | 99.4% | 20.0 | LOW | ❌ |
| usuario-8 | disgust | 99.6% | 60.0 | MEDIUM | ✅ |
| usuario-9 | disgust | 87.0% | 60.0 | MEDIUM | ✅ |
| usuario-10 | disgust | 99.8% | 60.0 | MEDIUM | ✅ |
| usuario-11 | sadness | 63.8% | 48.7 | MEDIUM | ✅ |
| usuario-12 | disgust | 97.2% | 60.0 | MEDIUM | ✅ |
| usuario-13 | joy | 98.6% | 0.0 | LOW | ❌ |
| usuario-14 | neutral | 99.6% | 20.0 | LOW | ❌ |
| usuario-15 | disgust | 99.8% | 60.0 | MEDIUM | ✅ |
| usuario-16 | sadness | 99.7% | 55.0 | MEDIUM | ✅ |
| usuario-17 | sadness | 99.8% | 55.0 | MEDIUM | ✅ |
| usuario-18 | sadness | 99.7% | 55.0 | MEDIUM | ✅ |
| usuario-19 | neutral | 57.0% | 30.0 | LOW | ❌ |
| usuario-20 | sadness | 90.8% | 55.0 | MEDIUM | ✅ |

| Top emotion | Count |
|---|---:|
| disgust | 8 |
| neutral | 6 |
| sadness | 5 |
| joy | 1 |

## Neutral folder (`audios/neutral/`)

**Expected category:** LOW · **Correct:** 7/20 (35%) · **False positives (MEDIUM):** 13/20 (65%)

| Audio | Top emotion | Confidence | SS | Category | Correct |
|---|---|---:|---:|---|:---:|
| usuario-1 | neutral | 99.8% | 20.0 | LOW | ✅ |
| usuario-2 | neutral | 99.9% | 20.0 | LOW | ✅ |
| usuario-3 | neutral | 99.9% | 20.0 | LOW | ✅ |
| usuario-4 | sadness | 75.3% | 55.0 | MEDIUM | ❌ |
| usuario-5 | disgust | 99.7% | 60.0 | MEDIUM | ❌ |
| usuario-6 | disgust | 98.0% | 60.0 | MEDIUM | ❌ |
| usuario-7 | disgust | 99.5% | 60.0 | MEDIUM | ❌ |
| usuario-8 | neutral | 99.9% | 20.0 | LOW | ✅ |
| usuario-9 | disgust | 99.6% | 60.0 | MEDIUM | ❌ |
| usuario-10 | neutral | 99.0% | 20.0 | LOW | ✅ |
| usuario-11 | disgust | 98.4% | 60.0 | MEDIUM | ❌ |
| usuario-12 | sadness | 50.4% | 57.3 | MEDIUM | ❌ |
| usuario-13 | disgust | 89.9% | 60.0 | MEDIUM | ❌ |
| usuario-14 | neutral | 99.7% | 20.0 | LOW | ✅ |
| usuario-15 | disgust | 99.8% | 60.0 | MEDIUM | ❌ |
| usuario-16 | sadness | 99.4% | 55.0 | MEDIUM | ❌ |
| usuario-17 | sadness | 46.6% | 39.5 | LOW | ✅ |
| usuario-18 | disgust | 91.9% | 60.0 | MEDIUM | ❌ |
| usuario-19 | sadness | 62.4% | 56.5 | MEDIUM | ❌ |
| usuario-20 | disgust | 99.8% | 60.0 | MEDIUM | ❌ |

| Top emotion | Count |
|---|---:|
| disgust | 9 |
| neutral | 6 |
| sadness | 5 |
| joy | 0 |

- Uso de CPU/GPU: Para la muestra de audios descrita anteriormente, basta con la CPU. No hay evidencia de la necesita de uso de gpu para el tipo de audio seleccionados.
- Promedio de duración en segundos "en caliente" data la muestra dada (40 audios): **3.182 segundos**
- Promedio de duración en segundos "semi-frio" (tiempo de carga de librerias, archivos, etc incluidos) para cada audio dada la muestra dada (40 audios): **14.34 segundos**
- ¿Duración de inferencia esperada (200 ms en caliente con el modelo ya cargado en memoria)?: **Localmente: NO**

## Conclusiones y recomendaciones:
El modelo funciona y entrega las emociones que necesitamos, pero hoy no cumple los requisitos para producción. En nuestras llamadas reales no logra distinguir a un cliente frustrado de uno tranquilo: acierta tanto como lanzar una moneda. Además, sin una tarjeta gráfica (GPU) tarda más de 10 veces el tiempo permitido. La causa principal es que el modelo **posiblemente** aprendió con videos de YouTube en español, y nuestras grabaciones son llamadas telefónicas colombianas, que suenan muy distinto. No recomendamos usarlo tal como está. Recomendamos adaptarlo con nuestras propias grabaciones antes de volver a evaluarlo.

- Hardware. El modelo no exige GPU para funcionar: todas las pruebas corrieron en CPU. Pero sí la exige para cumplir la latencia. Los requisitos 1 y 2 no pueden cumplirse a la vez con este modelo completo. Una alternativa que reduciría costos es usar solo las capas intermedias del modelo con un clasificador propio, lo que bajaría el cómputo de 2 a 3 veces.

- Robustez acústica en español. Es el principal incumplimiento. Con 20 audios de frustración y 20 neutrales, el modelo clasificó como “frustración o insatisfacción” al 65% de ambos grupos. No separa las clases: la exactitud balanceada es de 50%, equivalente al azar. Además, es excesivamente confiado: la mayoría de las predicciones superan el 97% de confianza, sean correctas o no. Las causas identificadas son tres:

- Entrenamiento: El modelo se entrenó con Spanish MEACorpus 2023 (YouTube, banda ancha, mayormente español peninsular), mientras que nuestras llamadas son telefónicas a 8 kHz con acento colombiano. Los propios autores advierten que el rendimiento cae con acentos marcados, audio de baja calidad y cambios de dominio. La emoción miedo tuvo solo 26 ejemplos de entrenamiento, así que sus predicciones no son confiables.

- Mapeo de emociones. El toolkit entrega exactamente seis emociones con sus probabilidades: anger, disgust, fear, joy, neutral, sadness. Esto permite construir la fórmula de Sentimiento (−1 a 1) asignando a cada emoción un valor de positividad (valencia). Al restar el valor de azar (1/6) a cada probabilidad, solo cuenta lo que cada emoción tiene por encima de una predicción aleatoria. Esto evita que el residuo repartido entre las cuatro emociones negativas sesgue el resultado. Si ninguna emoción supera el azar, el fragmento se marca como incierto y no se usa para decidir. Los valores de valencia son un punto de partida y deben calibrarse con datos etiquetados. Con el comportamiento actual del modelo, esta fórmula daría Sentimiento negativo también en llamadas tranquilas. Con respecto al valor Sentiment Score de 0 a 100 (LOW / MEDIUM / HIGH), ya existe la fórmula equivalente: mide intensidad de riesgo en lugar de positividad.

