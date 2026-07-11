# 音声パイプライン（多聴用TTS・M4で恒久化）

> 旧セッションのscratchpadから救出（2026-07-11）し、可搬化済み。仕様の正= `decisions.md` G13。
> 新プロジェクトでは `tools/audio/` としてルート直下に配置する（`batch_season.sh` はその配置を前提にルートを自動解決。`PROJ_ROOT` で上書き可）。

## 依存
- `edge-tts`（`pip install edge-tts`。venvの場合は `EDGE_TTS_BIN=/path/to/edge-tts` で指定）
- `ffmpeg`

## 使い方
```bash
# 1話生成: gen_episode.sh <episode.md> <rate> <out.mp3> [段落間ポーズ秒=0.9]
tools/audio/gen_episode.sh season1/chapter01/ep001.md -10% _audio/season1/chapter01/ep001.mp3 0.6

# 季ごと一括（既存ファイルはskip・再開可能）: 速度は季で自動（S1=-10% / S2=-5% / S3=+0%）
tools/audio/batch_season.sh 1
```

## 仕様（G13準拠）
- 声=en-GB-RyanNeural（単一ナレーター）・frontmatterタイトル読み上げ→0.8s→本文・段落間0.6s・24kHz mono 48kbps mp3
- 出力= `_audio/season{N}/chapter{NN}/ep{NNN}.mp3`（permalinkミラー・gitignore対象）
- 名前の発音置換（ソース.mdは無改変・title+bodyに適用）: Ako-chan→Ahko-chan／Suke-san→Suh-keh-san／Adelie→Ah-day-lee

## ⚠️ v2で生成する前に必ずやること
1. **同綴異音語の再走査**: スクリプト内の修正のうち `tear/tears→tier/tiers`（涙）はv1で全27箇所が「涙」だったための全域置換、`wind backward`（動詞ワインド）と `content`（満足）は**v1の特定話にだけあった局所修正**。v2本文は全て新規のため、生成前に対象語（tear/wind/content/read/lead/row/desert/live/bows 等）を全話grepして respell() を更新する。
2. 新キャラ・新固有名（もしあれば）のTTS試聴チェック。
3. 速度・話者を変える場合は G13 を先に改定する（現状維持が既定）。
