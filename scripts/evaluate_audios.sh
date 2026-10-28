export HF_HUB_OFFLINE=1
find audios -type f -name "*.wav" | sort | {
  total=0; n=0
  while read -r f; do
    inicio=$(date +%s.%N)
    echo "=== $f"
    echo "Inicio: $(date '+%Y-%m-%d %H:%M:%S.%3N')"
    speech-emotion --audio "$f" --language es --mode audio --device cpu --model-config model.json
    fin=$(date +%s.%N)
    dur=$(awk -v a="$inicio" -v b="$fin" 'BEGIN{printf "%.3f", b-a}')
    echo "Fin:    $(date '+%Y-%m-%d %H:%M:%S.%3N')  |  Duración: ${dur} s"
    total=$(awk -v t="$total" -v d="$dur" 'BEGIN{printf "%.3f", t+d}')
    n=$((n+1))
  done
  echo "================================================"
  if [ "$n" -gt 0 ]; then
    echo "Audios procesados: $n"
    echo "Tiempo total:      ${total} s"
    echo "Tiempo promedio:   $(awk -v t="$total" -v n="$n" 'BEGIN{printf "%.3f", t/n}') s"
  else
    echo "No se encontraron archivos .wav"
  fi
} 2>&1 | tee resultados.txt