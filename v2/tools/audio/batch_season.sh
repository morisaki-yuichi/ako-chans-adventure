#!/usr/bin/env bash
# Usage: batch_season.sh <season-number>
set -euo pipefail
# プロジェクトルート: 既定=このスクリプトの2階層上（tools/audio/ 配置前提）。PROJ_ROOT で上書き可
PROJ="${PROJ_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}"
GEN="$(cd "$(dirname "$0")" && pwd)/gen_episode.sh"

S="$1"
case "$S" in
  1) RATE="-10%";; 2) RATE="-5%";; 3) RATE="+0%";;
  *) echo "bad season $S"; exit 1;;
esac

mapfile -t FILES < <(ls "$PROJ/season$S"/chapter*/ep*.md | sort)
total=${#FILES[@]}
echo "[batch] season $S  rate $RATE  episodes=$total  start=$(date +%T)"
i=0
for src in "${FILES[@]}"; do
  i=$((i+1))
  rel="${src#$PROJ/}"                 # season1/chapter01/ep001.md
  out="$PROJ/_audio/${rel%.md}.mp3"   # _audio/season1/chapter01/ep001.mp3
  mkdir -p "$(dirname "$out")"
  if [ -s "$out" ]; then echo "[$i/$total] skip (exists) ${rel%.md}"; continue; fi
  "$GEN" "$src" "$RATE" "$out" 0.6 >/dev/null 2>>"$PROJ/_audio/batch_s$S.err" \
    && echo "[$i/$total] OK ${rel%.md}" \
    || echo "[$i/$total] FAIL ${rel%.md}"
done
echo "[batch] season $S DONE  end=$(date +%T)  files=$(find "$PROJ/_audio/season$S" -name '*.mp3' | wc -l)"
