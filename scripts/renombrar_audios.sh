#!/usr/bin/env bash
# Renombra los audios a: frustracion-banco-occidente-usuario-{indice}.{ext}
# Uso:
#   ./renombrar_audios.sh              -> simulación (no cambia nada)
#   APLICAR=1 ./renombrar_audios.sh    -> renombra de verdad
#   ORDEN=fecha ./renombrar_audios.sh  -> ordena por fecha de modificación (por defecto: nombre)

set -euo pipefail

DIR="${1:-./audios/neutral}"
PREFIJO="neutral-banco-occidente-usuario"
APLICAR="${APLICAR:-1}"
ORDEN="${ORDEN:-nombre}"

cd "$DIR" || { echo "No existe la carpeta: $DIR"; exit 1; }

EXT_REGEX='.*\.(wav|mp3|m4a|ogg|oga|opus|flac|aac|wma|webm|amr|aiff|aif)$'

# Listar solo archivos de audio (sin entrar a subcarpetas)
if [[ "$ORDEN" == "fecha" ]]; then
  mapfile -d '' archivos < <(find . -maxdepth 1 -type f -regextype posix-extended -iregex "$EXT_REGEX" -printf '%T@\t%f\0' | sort -z -n | cut -z -f2-)
else
  mapfile -d '' archivos < <(find . -maxdepth 1 -type f -regextype posix-extended -iregex "$EXT_REGEX" -printf '%f\0' | sort -z -V)
fi

total=${#archivos[@]}
[[ $total -eq 0 ]] && { echo "No se encontraron audios en $DIR"; exit 0; }
echo "Audios encontrados: $total (orden: $ORDEN)"

# Fase 1: nombres temporales (evita choques si algún archivo ya tiene el nombre destino)
declare -a temporales destinos
i=1
for f in "${archivos[@]}"; do
  ext="${f##*.}"; ext="${ext,,}"
  destino="${PREFIJO}-${i}.${ext}"
  echo "  $f  ->  $destino"
  if [[ "$APLICAR" == "1" ]]; then
    tmp=".tmp_renombrar_${i}_$$.${ext}"
    mv -n -- "$f" "$tmp"
    temporales+=("$tmp"); destinos+=("$destino")
  fi
  ((i++))
done

# Fase 2: nombres finales
if [[ "$APLICAR" == "1" ]]; then
  for k in "${!temporales[@]}"; do
    mv -n -- "${temporales[$k]}" "${destinos[$k]}"
  done
  echo "Listo: $total archivos renombrados."
else
  echo "Simulación. Para aplicar los cambios: APLICAR=1 $0"
fi
