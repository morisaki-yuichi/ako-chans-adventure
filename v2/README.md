# Ako-chan's Adventure v2 — 全面再執筆・移行ワークスペース

**目的**: v1（現行・全300話公開済み）の全面再執筆に向けて、(1) 残すべき資産の抽出、(2) 不足していた設計の追加、(3) 執筆に必要な情報が揃った状態、を作る。
**位置づけ**: 本ディレクトリは一時的な移行用ワークスペース。準備完了後に**独立した1つのプロジェクトとして外へ移動**し、そこで全シーズン・全エピソードを再執筆する（v1のような新旧混在の部分改稿はしない）。
**Jekyll**: `_config.yml` の `exclude` に `v2/` 登録済み（公開サイトには出ない）。

---

## 読む順序（新セッション向け）

| # | ファイル | 内容 |
|---|---------|------|
| 1 | `planning/decisions.md` | **確定判断レジストリ**（最優先。すべての文書はここに従う） |
| 2 | `planning/true-requirements.md` | 真の要求分析（指摘→根本原因→v2要件 R1〜R12） |
| 3 | `planning/chronology.md` | マスター年表（年齢・成長・寿命の一元管理） |
| 4 | `planning/characters.md` | キャラクターバイブル v2（新外見・発話権・状態年表） |
| 5 | `planning/series-arc.md` | シリーズ縦糸（ループ・首輪・日記・能力モデル・季の自己完結契約） |
| 6 | `planning/world-core.md` | 世界の物理・道具（異変・Pod・ガジェット・移動手段・継続性総覧） |
| 7 | `planning/season-redesign-briefs.md` | S1/S2/S3 再設計ブリーフ（keep / 変更 / 規模） |
| 8 | `planning/s1.md` / `s2.md` / `s3.md` | **各季の章構成v2（M2承認済み骨子）** |
| 9 | `planning/writing-guide-v2.md` | 執筆ガイド v2（統合版・自己完結） |
| 9 | `planning/quote-bank.md` | 確定台詞キュレーション（T1逐語必須／T2推奨／T3ビートのみ） |
| 10 | `planning/keep-register.md` | v1から持ち込む資産台帳（ルール・名場面ビート・教訓） |
| 11 | `process/writing-system.md` | 執筆システム v2（義務台帳・グリッド仕様・工程・通読レビュー） |
| 12 | `planning/open-questions.md` | 未決事項キュー |

補助: `planning/quote-bank-raw.md` = v1 timeline.md の🔒行 全266件の機械抽出（原簿・監査用）。

---

## 作業フェーズとチェックリスト

### M0 分析・基本意思決定 ✅（2026-07-11）
- [x] v1全設計文書・診断・監査・本文サンプルの精査
- [x] 真の要求分析（true-requirements.md）
- [x] ユーザー確定4件（語数レベル連動＋話数可変／年表=現行＋氷4〜5年／発話=Luca解禁+Dango取っておき／綴り=Dalu・Luca維持）
- [x] ワークスペース構築・Jekyll除外
- [x] 未決キュー第1回判断（2026-07-11: Dalu=c案／新リポ非公開／Kara-san続投／Dango=①+③／S2=A2中心・語彙1500／タイトル継承／S1ペイオフ方向性承認 → D14〜D20）

### M1 設計文書の完成 ✅（2026-07-11）
- [x] `quote-bank.md` 作成（🔒266件を3層キュレーション: T1逐語必須／T2逐語推奨／T3ビートのみ）
- [x] `world-core.md` 作成（v1 world.md の残要素——異変の正体・4段階・二重構造・Pod仕様・ガジェット・移動手段・継続性総覧——をv2確定事項で更新して移植）
- [x] `writing-guide-v2.md` 統合版（v1ガイド＋差分を一本化・自己完結。`writing-guide-v2-delta.md` は廃止）
- [x] characters.md の TBD 解消（Dango取っておき=D17で確定。残る具体化はM3の設計事項のみ）

### M2 シーズン骨子（章構成の確定）✅（2026-07-11・ユーザー承認=D21）
- [x] S1 章構成 v2 → `planning/s1.md`（98話・震源スレッド・救助ラダー・帰路8話）
- [x] S2 章構成 v2 → `planning/s2.md`（92話・見習いアーク・洞窟発見=震源回収）
- [x] S3 章構成 v2 → `planning/s3.md`（87話・命名ラダー・Pod直す手・v0未熟明示）
- [x] 伏線→回収レジストリの章住所 → `series-arc.md` §2-7

### M3 エピソードグリッド（全話設計）✅（2026-07-11・全グリッド承認=D22）
- [x] 各季 episode-list v2 → **S1=✅（Ep1〜98）／S2=✅（Ep99〜190）／S3=✅（Ep191〜277）**
- [x] 話数・通し番号確定 → **全277話**（98＋92＋87・34章）
- [x] 台帳4冊をグリッドから生成 → `planning/ledgers.md`
- [x] Dango取っておき確定 → ①S2 Ep175 *"Stay."*／③S3 Ep275 *"Home."*（quote-bank §1-17）

### M4 移行最終確認 ✅（2026-07-11）
- [x] v1資産の取りこぼしチェック → `keep-register.md` §G監査（§A〜F全項目の移植先確認。発見: episodes.mdはv1ルートに非実在→M5で入口再確認）
- [x] インフラ計画確定 → `planning/migration-checklist.md` §0（執筆中=新リポ非公開・残置3問は計画に組込み）
- [x] サイト骨格の複製リスト確定 → `planning/migration-checklist.md` §2〜4（実在確認済みファイル一覧＋移動後タスク）
- [x] 音声パイプラインの恒久化 → `tools/audio/`（旧scratchpadから救出・venvパス除去・可搬化・README＋生成前チェック付き）

### M5 独立プロジェクト化（移動）— 次の作業（要: リポジトリ名の決定 → open-questions #3）
- [ ] `v2/` を新ロケーションへ移動（例: `~/projects/ako-chans-adventure-v2/`）
- [ ] `git init`（または新リポジトリ作成）・初回コミット
- [ ] サイト骨格を複製し、v2用に文言・設定を更新
- [ ] 新プロジェクトの `CLAUDE.md` をルート版に昇格（本ワークスペースの CLAUDE.md を基に）
- [ ] 執筆開始（`process/writing-system.md` の工程で章単位）

---

## 運用ルール

1. **v1は読み取り専用の参照元**。`season*/`・`planning/`・`_includes/` 等のv1ファイルはこの移行作業では編集しない（例外: 今回の `_config.yml` exclude 追加のみ）。
2. **v2文書は自己完結**させる。移動後は v1 リポジトリも Claude メモリも参照できない前提で、必要な事実はすべて v2/ 内に書き写す。
3. **散文は移植しない。ビートと🔒台詞だけを移植する**（トーン新旧混在の再発防止。詳細: true-requirements R3）。
4. 未決事項は必ず `planning/open-questions.md` に積む。確定したら `decisions.md` へ昇格し、日付を付す。
5. 各フェーズ完了時に本ファイルのチェックボックスを更新する。
