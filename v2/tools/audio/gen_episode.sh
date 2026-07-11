#!/usr/bin/env bash
# Usage: gen_episode.sh <episode.md> <rate e.g. -10%> <output.mp3> [pause_seconds]
set -euo pipefail
# edge-tts binary: PATH上の edge-tts を既定とし、venv利用時は EDGE_TTS_BIN で上書き
BIN="${EDGE_TTS_BIN:-edge-tts}"
VOICE="en-GB-RyanNeural"

SRC="$1"; RATE="$2"; OUT="$3"; PAUSE="${4:-0.9}"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

# name respellings for TTS only (applied to title + body)
respell() { sed -e 's/Ako-chan/Ahko-chan/g' -e 's/Suke-san/Suh-keh-san/g' -e 's/Adelie/Ah-day-lee/g' \
                -e 's/\bTears\b/Tiers/g' -e 's/\btears\b/tiers/g' -e 's/\bTear\b/Tier/g' -e 's/\btear\b/tier/g' \
                -e 's/wind backward/wined backward/g' -e 's/\bcontent\b/cun-tent/g'; }

# 1) extract body (after 2nd ---)
awk '/^---/{n++; if(n==2){found=1; next}} found' "$SRC" | respell > "$WORK/body.txt"

# 1b) extract frontmatter title (strip leading "title:" and surrounding quotes)
TITLE="$(sed -n 's/^title:[[:space:]]*//p' "$SRC" | head -1 | sed -e 's/^"//' -e 's/"[[:space:]]*$//' | respell)"

# split into paragraphs on blank lines -> para_000.txt ...
awk 'BEGIN{p=0} /^[[:space:]]*$/{if(buf!=""){printf "%s",buf > sprintf("'"$WORK"'/para_%03d.txt",p);p++;buf=""} next} {buf=buf $0 "\n"} END{if(buf!=""){printf "%s",buf > sprintf("'"$WORK"'/para_%03d.txt",p)}}' "$WORK/body.txt"

# silence clips matching edge-tts format (24k mono mp3): 0.6s between paragraphs, 0.8s after title
ffmpeg -nostdin -v error -f lavfi -t "$PAUSE" -i anullsrc=r=24000:cl=mono -c:a libmp3lame -b:a 48k "$WORK/sil.mp3"
ffmpeg -nostdin -v error -f lavfi -t 0.8     -i anullsrc=r=24000:cl=mono -c:a libmp3lame -b:a 48k "$WORK/sil_title.mp3"

# title clip, then build concat list: title + 0.8s + paragraphs (0.6s between)
: > "$WORK/list.txt"
"$BIN" --voice "$VOICE" --rate="$RATE" --text "$TITLE" --write-media "$WORK/title.mp3" >/dev/null 2>&1
echo "file '$WORK/title.mp3'" >> "$WORK/list.txt"
echo "file '$WORK/sil_title.mp3'" >> "$WORK/list.txt"
i=0
for f in "$WORK"/para_*.txt; do
  [ -s "$f" ] || continue
  out="$WORK/$(printf 'p%03d.mp3' "$i")"
  "$BIN" --voice "$VOICE" --rate="$RATE" --file "$f" --write-media "$out" >/dev/null 2>&1
  [ "$i" -gt 0 ] && echo "file '$WORK/sil.mp3'" >> "$WORK/list.txt"
  echo "file '$out'" >> "$WORK/list.txt"
  i=$((i+1))
done

# concat (re-encode to keep clean timestamps)
ffmpeg -nostdin -v error -f concat -safe 0 -i "$WORK/list.txt" -c:a libmp3lame -b:a 48k "$OUT"
echo "OK: $OUT  (paragraphs=$i)"
