# EmpaIA - SPEECH EMOTION RECOGNITION

### Disclaimer 
_THIS IS AN EXPERIMENTAL REPOSITORY. 
THESE PRE-TRAINED ALGORITHMS DOES NOT ENSURE A 100% ACCURACY IN EMOTION RECOGNITION
AND MOST OF THEM WOULD RETURN FALSE POSITIVES IN SOME DEGREE.
THE GOAL OF THIS REPO IS TO IDENTIFY AND TEST PRE-TRAINED MODELS FROM HUGGING FACE
AS PART OF THE ARCHITECTURAL DESIGN OF EMPATIA_


### Benchmarking

#### Dataset
Basado en los audios/transcripciones generados en entornos productivos, se generaron set de audios de acuerdo
a las caracteristicas de entonación de los usuarios y a la escala de análisis de sentimiento existente (neutral, frustración, otro).
Los dataset cumple con las siguientes caracteristicas para poder evaluar la precision de los modelos de acuerdo a los requisitos
funcionales y no funcionales del analisis de sentimiento de empatia:

- Duración entre 2 segundos y 13 segundos.
- Tamaño de 20 audios por escala (muestra pequeña debido al margén de tiempo y limitaciones de los recursos).
- Formato .wav

**Modelo UMUTeam/w2v-bert-emotion-es** 
- Entorno de ejecución: local
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



