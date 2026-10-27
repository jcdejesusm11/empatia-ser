# EmpaIA - SPEECH EMOTION RECOGNITION

### Disclaimer 
_THIS IS AN EXPERIMENTAL REPOSITORY. 
THESE PRE-TRAINED ALGORITHMS DOES NOT ENSURE a 100% ACCURACY IN EMOTION RECOGNITION
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
