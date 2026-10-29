

# Como ejecutar y evaluar modelos de inferencia bajo la carpeta src

## w2v-bert-emotion-es.py

## wav2vec2-base-finetuned-sentiment-mesd.py

Desde la raiz del projecto, ejecutar el siguietne comando:

- uv run python ./src/wav2vec2-base-finetuned-sentiment-mesd.py ./audios --online

Si quieres almacenar el resultado en un archivo tipo json, debes ejecutar:

- uv run python ./src/wav2vec2-base-finetuned-sentiment-mesd.py ./audios --ventana 2 --salida nombre-de-archivo.json

- uv run python ./src/wav2vec2-base-finetuned-sentiment-mesd.py ./audios --ventana 3 --salida nombre-de-archivo.json

- uv run python ./src/wav2vec2-base-finetuned-sentiment-mesd.py ./audios --ventana 4 --salida nombre-de-archivo.json