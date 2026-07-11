# v2 ワークスペース規約（このディレクトリ配下の作業ルール）

本ディレクトリは「Ako-chan's Adventure」**全面再執筆（v2）の移行ワークスペース**。後日、独立プロジェクトとして外部へ移動する。

## 最優先ルール

1. **正典は `v2/planning/decisions.md`**。ルートの `CLAUDE.md`・`planning/*` とv2文書が食い違う場合、v2配下の作業では v2 文書が正。
2. **v1（`season*/`・`planning/`・サイト骨格）は読み取り専用の参照元**。v2作業でv1ファイルを編集しない。
3. **自己完結原則**: v2文書に書く事実は、v1やClaudeメモリを参照しなくても成立する形で書き写す（移動後にv1が手元にない前提）。
4. **散文非移植**: v1本文からコピーしてよいのは「ビート（何が起きるか）」と「🔒確定台詞」のみ。地の文の再利用は禁止（新旧トーン混在の再発防止）。
5. 未決事項は `planning/open-questions.md` へ。確定したら `decisions.md` に日付つきで昇格。
6. 進捗は `README.md` のフェーズチェックリスト（M0〜M5）を更新して管理する。

## 参照マップ

- 作業全体像・フェーズ → `README.md`
- 要件の根拠 → `planning/true-requirements.md`（R1〜R12）
- 年齢・寿命・経過年数 → `planning/chronology.md`
- キャラ設定（外見・発話権・呼称） → `planning/characters.md`
- ループ・首輪・日記・能力モデル・季の契約 → `planning/series-arc.md`
- 語数帯・文法ティア・執筆規則差分 → `planning/writing-guide-v2-delta.md`
- v1資産（ルール・🔒台詞・名場面・教訓） → `planning/keep-register.md`
- 執筆工程・台帳・グリッド仕様 → `process/writing-system.md`

## 本ワークスペースで書かないもの

- エピソード本文（執筆は独立プロジェクト化＝M5後に開始）
- v1の修正（v1は凍結。バグを見つけたら keep-register の教訓欄に記録するのみ）
