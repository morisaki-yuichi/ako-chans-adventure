# 移行チェックリスト — M5独立化の実行手引き（M4確定 2026-07-11）

> M4で確定した「何を持って出るか・出た後に何をするか」。実行はM5（要: リポジトリ名の決定 → `open-questions.md` #3）。

## 0. インフラ計画（確定事項の整理）

| 項目 | 方針 |
|------|------|
| リポジトリ | **新リポジトリ・非公開**で執筆（D15）。v1サイトは完成まで現状維持 |
| 公開方式 | v2完成時に判断（v1差し替え or 新URL → open-questions #1） |
| 音声 | 執筆完了後にローカル生成（`tools/audio/`・恒久化済み）。ホスティング先は完成時判断 |
| 通し番号・permalink | `season{N}/chapter{NN}/ep{NNN}` 方式を継承。S2=Ep099〜190・S3=Ep191〜277 の新番号で生成（新リポなのでv1と衝突しない） |

## 1. 移動手順（M5）

```bash
# 1) v2/ を新ロケーションへ（例）
mv /home/u1/projects/ako-chans-adventure/v2 /home/u1/projects/<新プロジェクト名>
cd /home/u1/projects/<新プロジェクト名>
# 2) 新リポジトリ化
git init && git add -A && git commit -m "v2: 移行ワークスペースを独立プロジェクト化（M5）"
# 3) v1側: v2/ の削除をコミット（v1リポジトリにはv2の全履歴が残る）
```

- 移動後、`planning/`・`process/`・`tools/` はそのままルート直下の構成になる。
- **v1リポジトリは凍結**（公開サイトの現状維持のみ。以後の作業はすべて新プロジェクト）。

## 2. v1から複製するファイル（実在確認済み 2026-07-11）

| 種別 | ファイル | 移動後の処理 |
|------|---------|-------------|
| レイアウト | `_layouts/default.html`・`_layouts/episode.html` | そのまま |
| インクルード | `_includes/season-cards.html`・`season-list.html`・`season-tabs.html` | **season-list.htmlのtitlesリストは章題継承（D19/D21）なので原則そのまま**。話数・Ep範囲のロジックはデータ駆動なので無変更 |
| CSS | `assets/css/main.css` | そのまま（Concept C=G15。`style.css`に改名しない） |
| Jekyll設定 | `_config.yml`・`_config_dev.yml` | **baseurl/url をリポ名確定後に更新**・exclude から `v2/` を外し `planning/`・`tools/` 等に整理 |
| Ruby | `Gemfile`・`Gemfile.lock` | そのまま |
| 音声試聴 | `serve_audio.py` | そのまま |
| その他 | `.gitignore` | `_audio/`・`_site/`・`vendor/`・`.bundle/` の無視を継承 |
| サイトページ | `index.md`・`season1.md`・`season2.md`・`season3.md` | **文言はv2確定値で書き直し**（等級・ネタバレ規則=G14。話数表現=98/92/87） |

⚠️ **`episodes.md` はv1ルートに存在しない**（v1 CLAUDE.mdの記述「episodes.mdは季チューザー」と実態に差異）。M5で入口構成を再確認する——現状は index.md（季カード）＋season{N}.md で完結している可能性が高い。入口が index のみで足りるならそのまま踏襲。

## 3. 複製しないもの

- `season1/ season2/ season3/`（v1本文＝散文非移植の原則D1。ビートと🔒はグリッド・quote-bankに移植済み）
- `planning/`（v1版。v2の `planning/` が正）
- `_audio/`・`_site/`・`vendor/`・`.bundle/`（生成物・依存）
- v1の `CLAUDE.md`（→ `v2/CLAUDE.md` を昇格・下記4）

## 4. 移動後の更新タスク

1. **CLAUDE.md昇格**: `v2/CLAUDE.md` をルート用に書き直す——「v1は読み取り専用」等の移行時規約を削除し、「読む順序（README準拠）→章サイクル（process/writing-system.md）→執筆規則（writing-guide-v2.md）」の恒常運用版へ。
2. **README.md**: M0〜M5チェックリストを「完了記録」節に格下げし、執筆進捗（章単位）の管理表を新設。
3. **_config.yml**: title/description/baseurl/url・exclude整理（planning/・process/・tools/・README.md 等）。
4. **サイトページ文言**: index・season{1,2,3}（G14: 入口=A1・各季導入=当該レベル・ネタバレ回避）。
5. **音声**: `tools/audio/README.md` の「生成前チェック」を執筆完了後に必ず実施（同綴異音語の再走査）。
6. **メモリ非依存の最終確認**: 新プロジェクトはClaudeメモリのディレクトリも変わる。必要事実がリポジトリ内の文書だけで完結していることを確認（keep-register §G監査で担保済み。新プロジェクト初回セッションでメモリに新プロジェクトの所在を記録する）。

## 5. 執筆開始（M5完了後）

1. レビュー粒度を決める（章ごと or 季まとめ → open-questions 工程内）。
2. `process/writing-system.md` の章サイクルで **S1 Ch1 から**。新デバイス（S1の新規話・季の声仕様）はパイロット2〜3話でトーン確認してから章単位へ。
3. 章完了ごと: Phase E（10話連読）／季完了ごと: Phase F（定量指標＋快感原理ゲート＋縦糸消化確認）。
