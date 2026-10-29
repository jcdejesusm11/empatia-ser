# EmpaIA - SPEECH EMOTION RECOGNITION

## Disclaimer 
_THIS IS AN EXPERIMENTAL REPOSITORY. 
THESE PRE-TRAINED ALGORITHMS DO NOT ENSURE A 100% ACCURACY IN SPEECH EMOTION RECOGNITION
AND MOST OF THEM WOULD RETURN FALSE POSITIVES OR NEGATIVES IN SOME DEGREE.
THE GOAL OF THIS REPO IS TO IDENTIFY AND TEST PRE-TRAINED MODELS FROM HUGGING FACE
AS PART OF THE ARCHITECTURAL DESIGN OF EMPATIA_

## Dataset
Basado en los audios/transcripciones generados en entornos productivos, se generaron set de audios de acuerdo
a las caracteristicas de entonación de los usuarios y a la escala de análisis de sentimiento existente (neutral, frustración, otro).
Los dataset cumple con las siguientes caracteristicas para poder evaluar la precision de los modelos de acuerdo a los requisitos
funcionales y no funcionales del analisis de sentimiento de empatia:

- Duración entre 2 segundos y 16 segundos.
- Tamaño de 20 audios por escala (muestra pequeña debido al margén de tiempo y limitaciones de los recursos).
- Formato .wav
- Frecuencia de muestreo: 8 kHz
- Mayormente audio télefonico.

## Entorno local
- CPU: 12TH Gen intel(R) Core (TM) i7-12800H - 2,40ghZ
- Memoria: 32 GB DDR5 SODIMM
- GPU: 1. Intel(R) UHD Graphics - 1,0/15,8 GB / 2. NVIDIA T600 Laptop GPU - 0,0/4 GB

## Evidencias

### Modelo UMUTeam/w2v-bert-emotion-es

- Descripción: modelo de clasificación de audio (SER) en español basado en wav2vec2-bert, etiquetado para reconocimiento de emociones.
- Autor(es): UMUTeam - Universidad de Murcia.
- Repositorio de modelo: https://github.com/NLP-UMUTeam/umuteam-speech-emotion
- Entorno de ejecución: **local**
- Resultados:

#### Frustación (`audios/frustracion/`)

**Categoría esperada:** MEDIUM · **Correctos:** 13/20 (65%) · **Falso negativos - incorrectos (LOW):** 7/20 (35%)

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

#### Neutral (`audios/neutral/`)

**Categoría esperada:** LOW · **Correcto:** 7/20 (35%) · **Falso negativos - incorrectos (MEDIUM):** 13/20 (65%)

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

#### Conclusiones y recomendaciones:
El modelo funciona y entrega las emociones que necesitamos, pero hoy no cumple los requisitos para producción. En nuestras llamadas reales no logra distinguir a un cliente frustrado de uno tranquilo: acierta tanto como lanzar una moneda. Además, sin una tarjeta gráfica (GPU) tarda más de 10 veces el tiempo permitido. La causa principal es que el modelo **posiblemente** aprendió con videos de YouTube en español, y nuestras grabaciones son llamadas telefónicas colombianas, que suenan muy distinto. No recomendamos usarlo tal como está. Recomendamos adaptarlo con nuestras propias grabaciones antes de volver a evaluarlo.

- Hardware. El modelo no exige GPU para funcionar: todas las pruebas corrieron en CPU. Pero sí la exige para cumplir la latencia. Los requisitos 1 y 2 no pueden cumplirse a la vez con este modelo completo. Una alternativa que reduciría costos es usar solo las capas intermedias del modelo con un clasificador propio, lo que bajaría el cómputo de 2 a 3 veces.

- Robustez acústica en español. Es el principal incumplimiento. Con 20 audios de frustración y 20 neutrales, el modelo clasificó como “frustración o insatisfacción” al 65% de ambos grupos. No separa las clases: la exactitud balanceada es de 50%, equivalente al azar. Además, es excesivamente confiado: la mayoría de las predicciones superan el 97% de confianza, sean correctas o no. Las causas identificadas son tres:

- Entrenamiento: El modelo se entrenó con Spanish MEACorpus 2023 (YouTube, banda ancha, mayormente español peninsular), mientras que nuestras llamadas son telefónicas a 8 kHz con acento colombiano. Los propios autores advierten que el rendimiento cae con acentos marcados, audio de baja calidad y cambios de dominio. La emoción miedo tuvo solo 26 ejemplos de entrenamiento, así que sus predicciones no son confiables.

- Mapeo de emociones. El toolkit entrega exactamente seis emociones con sus probabilidades: anger, disgust, fear, joy, neutral, sadness. Esto permite construir la fórmula de Sentimiento (−1 a 1) asignando a cada emoción un valor de positividad (valencia). Al restar el valor de azar (1/6) a cada probabilidad, solo cuenta lo que cada emoción tiene por encima de una predicción aleatoria. Esto evita que el residuo repartido entre las cuatro emociones negativas sesgue el resultado. Si ninguna emoción supera el azar, el fragmento se marca como incierto y no se usa para decidir. Los valores de valencia son un punto de partida y deben calibrarse con datos etiquetados. Con el comportamiento actual del modelo, esta fórmula daría Sentimiento negativo también en llamadas tranquilas. Con respecto al valor Sentiment Score de 0 a 100 (LOW / MEDIUM / HIGH), ya existe la fórmula equivalente: mide intensidad de riesgo en lugar de positividad.

### Modelo harshit345/xlsr-wav2vec-speech-emotion-recognition 
- Descripción: modelo de clasificación de audio (SER) basado en wav2vec 2.0 XLSR-53. La información en su ficha es engañosa e inconsistente pues la etiqueta de dataset es un corpus griego de habla actuada NO español.
**Ademas es desactualizado (su ultima actualización fue hace 5 años).** y necesita mucha actualización técnica para adaptarlo a los escenarios requeridos.
- Autor(es): 1 solo contributor.

#### Conclusiones y recomendaciones
No se recomienda usar dicho modelo en entornos productivos.

### Modelo somosnlp-hackathon-2022/wav2vec2-base-finetuned-sentiment-mesd
- Descripción: modelo de clasificación de audio (SER) en español (Méxicano) basado en ajuste fino (o "fine-tuning") sobre la versión de facebook/wav2vec2-base. Utiliza como dataset de entrenamiento la base de datos del discurso emocional Mexicano (MESD en inglés).
Utilizarón muestra de audios de 1 segundo de duración grabados o generados bajo condiciones especiales (
- Autor(es): 3 contributores
- Repositorio de modelo: N/A
- Entorno de ejecución: **local**
- Resultados:

#### Frustración (`audios/frustracion/`)

**Categoría esperada:** MEDIUM · **Correctos (MEDIUM):** 7/20 (35%) · **Correctos pero sobreestimados  -  (HIGH):** 8/20 (40%) · **Falso negativos - incorrectos (LOW):** 5/20 (25%)

| Audio | Top emotion | Confidence | SS | Category | Correct |
|---|---|---:|---:|---|:---:|
| usuario-1 | anger | 84.0% | 95.0 | HIGH | ⚠️ |
| usuario-2 | anger | 40.7% | 77.7 | HIGH | ⚠️ |
| usuario-3 | neutral | 89.5% | 20.0 | LOW | ❌ |
| usuario-4 | anger | 87.6% | 95.0 | HIGH | ⚠️ |
| usuario-5 | neutral | 62.9% | 25.5 | LOW | ❌ |
| usuario-6 | joy | 43.1% | 28.1 | LOW | ❌ |
| usuario-7 | anger | 84.1% | 95.0 | HIGH | ⚠️ |
| usuario-8 | anger | 35.9% | 69.3 | MEDIUM | ✅ |
| usuario-9 | neutral | 48.5% | 27.5 | LOW | ❌ |
| usuario-10 | disgust | 39.3% | 40.4 | MEDIUM | ✅ |
| usuario-11 | disgust | 88.0% | 60.0 | MEDIUM | ✅ |
| usuario-12 | disgust | 69.5% | 60.0 | MEDIUM | ✅ |
| usuario-13 | disgust | 85.8% | 60.0 | MEDIUM | ✅ |
| usuario-14 | neutral | 73.9% | 20.0 | LOW | ❌ |
| usuario-15 | disgust | 82.0% | 60.0 | MEDIUM | ✅ |
| usuario-16 | anger | 62.7% | 93.7 | HIGH | ⚠️ |
| usuario-17 | disgust | 73.4% | 60.0 | MEDIUM | ✅ |
| usuario-18 | anger | 73.5% | 95.0 | HIGH | ⚠️ |
| usuario-19 | disgust | 46.4% | 72.7 | HIGH | ⚠️ |
| usuario-20 | fear | 60.7% | 75.0 | HIGH | ⚠️ |

| Top emotion | Count |
|---|---:|
| anger | 7 |
| disgust | 7 |
| neutral | 4 |
| fear | 1 |
| joy | 1 |

#### Neutral (`audios/neutral/`)

**Categoría esperada:** LOW · **Correctos (LOW):** 4/20 (20%) · **Falsos negativos (MEDIUM):** 11/20 (55%) · **Falsos negativos (HIGH):** 5/20 (25%)

| Audio | Top emotion | Confidence | SS | Category | Correct |
|---|---|---:|---:|---|:---:|
| usuario-1 | disgust | 55.3% | 60.4 | MEDIUM | ❌ |
| usuario-2 | disgust | 51.9% | 56.0 | MEDIUM | ❌ |
| usuario-3 | neutral | 90.5% | 20.0 | LOW | ✅ |
| usuario-4 | sadness | 79.9% | 55.0 | MEDIUM | ❌ |
| usuario-5 | neutral | 89.6% | 20.0 | LOW | ✅ |
| usuario-6 | neutral | 86.4% | 20.0 | LOW | ✅ |
| usuario-7 | anger | 77.1% | 95.0 | HIGH | ❌ |
| usuario-8 | anger | 72.4% | 95.0 | HIGH | ❌ |
| usuario-9 | anger | 55.0% | 68.7 | MEDIUM | ❌ |
| usuario-10 | anger | 66.2% | 95.0 | HIGH | ❌ |
| usuario-11 | disgust | 46.6% | 35.4 | LOW | ✅ |
| usuario-12 | anger | 68.6% | 84.5 | HIGH | ❌ |
| usuario-13 | fear | 61.5% | 71.5 | HIGH | ❌ |
| usuario-14 | sadness | 27.8% | 63.7 | MEDIUM | ❌ |
| usuario-15 | sadness | 44.5% | 57.6 | MEDIUM | ❌ |
| usuario-16 | sadness | 44.8% | 64.8 | MEDIUM | ❌ |
| usuario-17 | sadness | 45.0% | 63.5 | MEDIUM | ❌ |
| usuario-18 | sadness | 82.2% | 55.0 | MEDIUM | ❌ |
| usuario-19 | sadness | 70.5% | 55.0 | MEDIUM | ❌ |
| usuario-20 | sadness | 75.4% | 55.0 | MEDIUM | ❌ |

| Top emotion | Count |
|---|---:|
| sadness | 8 |
| anger | 5 |
| disgust | 3 |
| neutral | 3 |
| fear | 1 |

- Uso de CPU/GPU: Para la muestra de audios descrita anteriormente, basta con la CPU. No hay evidencia de la necesita de uso de gpu para el tipo de audio seleccionados.
- Promedio de duración en segundos "en caliente" data la muestra dada (40 audios): **0.3623 segundos - 362.3 ms**
- Promedio de duración en segundos "semi-frio" (tiempo de carga de librerias, archivos, etc incluidos) para cada audio dada la muestra dada (40 audios): **N/A**
- ¿Duración de inferencia esperada (200 ms en caliente con el modelo ya cargado en memoria)?: **Localmente: Probablemente si la duración de los audios son entre 2 y 4 segundos. Audios mayores a 5 segundos supera el umbral. En el experimento se evidencia que: < 200 ms: 13/40 (32%)**.

  #### Conclusiones y recomendaciones

  El modelo _somosnlp-hackathon-2022/wav2vec2-base-finetuned-sentiment-mesd_ es mucho mejor en atencia o duración "en caliente" que el modelo _harshit345/xlsr-wav2vec-speech-emotion-recognition_ para el mismo set de datos.

  | Audios | Cantidad | Promedio | Mediana | p95 | Bajo 200 ms |
  |---|---:|---:|---:|---:|---:|
  | De 3 a 5 s | 8 | 196 ms | 196 ms | — | 5/8 (63%) |
  | Todos (0.8 a 23.4 s) | 40 | 362 ms | 254 ms | 861 ms | 13/40 (32%) |

  | Duración del fragmento | Latencia estimada | Cumple < 200 ms |
  |---|---:|:---:|
  | 3 s | ~144 ms | ✅ |
  | 4 s | ~193 ms | ✅ (al límite) |
  | 5 s | ~242 ms | ❌ |

  Sin embargo, la precisión de este modelo es igual o peor que _harshit345/xlsr-wav2vec-speech-emotion-recognition_. **No logra identificar/clasificar claramente los audios neutrales correctamente.
  Solo 20% fueron identificados correctamente, lo cual es una taza muy baja para los requisitos o umbrales esperados en empatia.**

  Se podría realizar una nueva iteración con este modelo pero con set de audios de entre 2 y 4 segundos de duración y volver a analizar los resultados.
