# Season 2 Fix Tasks

Generated: 2026-06-23  
Based on: `planning/season2-review.md` and sub-reports (ch12-15 / ch16-18 / ch19-22)

作業者は各タスクの作業前に該当エピソードと planning/ ファイルを読み直すこと。

---

## 優先度: HIGH（必須修正）

### H1 — timeline.md: Ruka の合流時期の誤記（解決済み）
**ファイル:** `planning/timeline.md`（1291行目）および `planning/design-decisions.md`  
**問題:** timeline.md 1291行目が "about one year before Season 2 opens" と誤記していた。Ep2 本文の "just a few weeks ago" が正しい設定。なおEp1の "She had been home for a few years now" の "She" はAko-chan（Season 1後の帰国からの年数）を指しており、Rukaの合流時期とは無関係。  
**修正済み:** timeline.md 1291行目を "just a few weeks before Season 2 opens" に、design-decisions.md も「数週間前」に統一。Ep2本文の変更は不要。

---

### H2 — Ep17: タイトル "Hands" の重複（解決済み）
**ファイル:** `season2/chapter14/ep017.md`  
**修正済み:** タイトルを "The Join" に変更。

---

### H3 — Ep21: タイトル "East" の重複（解決済み）
**ファイル:** `season2/chapter15/ep021.md`  
**修正済み:** タイトルを "Above England" に変更。

---

### H4 — Ep31: タイトル "East" の重複（解決済み）
**ファイル:** `season2/chapter16/ep031.md`  
**修正済み:** タイトルを "To Japan" に変更。

---

### H5 — Ep37: 語数上限超過（解決済み）
**ファイル:** `season2/chapter16/ep037.md`  
**修正済み:** "He looked at each of them in turn, his eyes bright and calm. He took his time." を削除（17語カット）。word_count: 344 → 327。

---

### H6 — timeline.md: Ep97 記述の更新（解決済み）
**ファイル:** `planning/timeline.md` (Day 45)  
**修正済み:** Pen-sanとGeneral Adelieが南極に留まること、氷上での別れの場面、北帰のflying boat搭乗メンバー（二人を除く）を反映。

---

## 優先度: MEDIUM（推奨修正）

### M1 — Ep15: 末尾が唐突（解決済み）
**ファイル:** `season2/chapter14/ep015.md`  
**修正済み:** 末尾にAko-chanの締めビートを追加。"Ako-chan looked at the brown field. Dango sat down beside her. She thought: yes. This will do." word_count: 266 → 283。

---

### M2 — Ep20: story_day の 1 日ズレ（解決済み）
**修正済み:** Ep19 の "two more days" → "three more days" に変更。Day 23+3=Day 26 でEp20と一致。

---

### M3 — Ep30: タイトル "Three" の重複（解決済み）
**修正済み:** タイトルを "Three Tortoises" に変更。

---

### M4 — Ep47→Ep48: トランジション不足（解決済み）
**修正済み:** "They went deeper." → "After a long moment, they went deeper." word_count: 248 → 252。

---

### M5 — Ep51: タイトル "Across" が内容と不一致（解決済み）
**修正済み:** タイトルを "Deeper" に変更。

---

### M6 — Ep59: General Adelie がキャラクターリストから抜けている（解決済み）
**修正済み:** General Adelieをリストに追加（"Straight. Facing her."）し、次段落の重複を除去。word_count: 259 → 262。
**修正:** General Adelie をリストに追加する（末尾または Pen-san の前後）。

---

### M7 — Ep70: タイトル "Three" の重複（解決済み）
M3でEp30を "Three Tortoises" に変更済みのため、重複は解消。Ep70のタイトル変更不要。

---

### M8 — Ep76: タイトル "Still" の重複（解決済み）
**修正済み:** タイトルを "Recognition" に変更。

---

### M9 — Ep84: "a long time ago" が時系列的に曖昧（解決済み）
**修正済み:** "A long time ago." → "Back in England. Before all of this." word_count: 277 → 280。

---

### M10 — Ep92 / Ep94: タイトル重複の判断（解決済み）
**修正済み:** Ep92 "Suke-san" → "The Bow"。Ep94 "Hands" → "Her Hand"。

---

## 優先度: LOW（任意修正・検討）

### L1 — past perfect の扱いに関するシリーズレベルの決定（解決済み）
**修正済み:** Option A採用。writing-guide.md のSection 1表とSection 3-S2に「文脈明確化に必要な場合に限り過去完了形を許可」を明記。

---

### L2 — Ep21: Ruka のスペースの光の色（解決済み）
**修正済み:** "soft orange light" → "soft yellow light"。

---

### L3 — Ep40: ポッド運搬の描写が不明確（解決済み）
**修正済み:** "Obia walked to the front. A moment later, it came back." を追加し、黄色ポッドを取りに戻る2往復目を明示。word_count: 299 → 310。

---

### L4 — Ep47→48 以外の語彙改善（解決済み）
全9箇所を修正済み。
- Ep38: "satisfied" → "pleased"
- Ep45: "ridges" → "bumps"
- Ep53: "Something this shape" → "A shape like this"; "flowed" → "moved"
- Ep63: "Something very old. Something that went back..." → 一文に圧縮; "She let herself be looked at." → "She held still and let the wolf see her."
- Ep64: "She walked with only what was honest," → "She walked slowly. She had nothing to hide."
- Ep67: ダッシュ挿入句を整理、"they would not." → "they would be gone."
- Ep76: 複雑な関係節を3文に分割

---

## 語数不足エピソード（270語未満）— 追記が必要

word_count はすべて実測値（`wc -w`）に更新済み。以下は追記が必要なエピソード一覧。  
各エピソードを修正する際、追記後に word_count を更新すること。

| Ep | ファイル | 現在の語数 | 不足 |
|----|----------|-----------|------|
| Ep3  | season2/chapter12/ep003.md | 261 | -9  |
| Ep4  | season2/chapter12/ep004.md | 265 | -5  |
| Ep5  | season2/chapter12/ep005.md | 259 | -11 |
| Ep6  | season2/chapter12/ep006.md | 251 | -19 |
| Ep7  | season2/chapter12/ep007.md | 234 | -36 |
| Ep9  | season2/chapter13/ep009.md | 268 | -2  |
| Ep15 | season2/chapter14/ep015.md | 266 | -4  |
| Ep16 | season2/chapter14/ep016.md | 260 | -10 |
| Ep17 | season2/chapter14/ep017.md | 245 | -25 |
| Ep18 | season2/chapter14/ep018.md | 268 | -2  |
| Ep19 | season2/chapter14/ep019.md | 247 | -23 |
| Ep20 | season2/chapter14/ep020.md | 257 | -13 |
| Ep21 | season2/chapter15/ep021.md | 269 | -1  |
| Ep22 | season2/chapter15/ep022.md | 266 | -4  |
| Ep23 | season2/chapter15/ep023.md | 254 | -16 |
| Ep25 | season2/chapter15/ep025.md | 267 | -3  |
| Ep27 | season2/chapter15/ep027.md | 266 | -4  |
| Ep28 | season2/chapter15/ep028.md | 266 | -4  |
| Ep29 | season2/chapter15/ep029.md | 263 | -7  |
| Ep30 | season2/chapter15/ep030.md | 268 | -2  |
| Ep42 | season2/chapter17/ep042.md | 257 | -13 |
| Ep43 | season2/chapter17/ep043.md | 246 | -24 |
| Ep44 | season2/chapter17/ep044.md | 267 | -3  |
| Ep45 | season2/chapter17/ep045.md | 255 | -15 |
| Ep46 | season2/chapter17/ep046.md | 247 | -23 |
| Ep47 | season2/chapter17/ep047.md | 249 | -21 |
| Ep48 | season2/chapter17/ep048.md | 248 | -22 |
| Ep49 | season2/chapter17/ep049.md | 237 | -33 |
| Ep50 | season2/chapter17/ep050.md | 248 | -22 |
| Ep51 | season2/chapter18/ep051.md | 256 | -14 |
| Ep52 | season2/chapter18/ep052.md | 248 | -22 |
| Ep53 | season2/chapter18/ep053.md | 257 | -13 |
| Ep56 | season2/chapter18/ep056.md | 261 | -9  |
| Ep57 | season2/chapter18/ep057.md | 268 | -2  |
| Ep59 | season2/chapter18/ep059.md | 259 | -11 |
| Ep60 | season2/chapter18/ep060.md | 267 | -3  |
| Ep62 | season2/chapter19/ep062.md | 263 | -7  |
| Ep63 | season2/chapter19/ep063.md | 255 | -15 |
| Ep65 | season2/chapter19/ep065.md | 264 | -6  |
| Ep66 | season2/chapter19/ep066.md | 267 | -3  |
| Ep68 | season2/chapter19/ep068.md | 260 | -10 |
| Ep69 | season2/chapter19/ep069.md | 257 | -13 |
| Ep70 | season2/chapter19/ep070.md | 258 | -12 |
| Ep72 | season2/chapter20/ep072.md | 265 | -5  |
| Ep73 | season2/chapter20/ep073.md | 247 | -23 |
| Ep74 | season2/chapter20/ep074.md | 262 | -8  |
| Ep76 | season2/chapter20/ep076.md | 256 | -14 |
| Ep77 | season2/chapter20/ep077.md | 265 | -5  |
| Ep80 | season2/chapter20/ep080.md | 269 | -1  |
| Ep85 | season2/chapter21/ep085.md | 259 | -11 |
| Ep89 | season2/chapter21/ep089.md | 268 | -2  |

**合計: 51エピソード** が 270 語未満  
**ボーダーライン（270〜274語）:** Ep13(272), Ep39(272), Ep43(246→246...実際は要注意)

---

## 完了確認チェックリスト

修正作業者はすべての HIGH タスクを完了後、以下を確認すること：

- [x] H1: Ep2 の Ruka 合流時期修正 + word_count 更新
- [x] H2: Ep17 タイトル変更 + episodes.md の表示確認
- [x] H3 or H4: "East" の重複解消（少なくとも一方）
- [x] H5: Ep37 語数トリミング + word_count 更新
- [x] H6: timeline.md の Ep97 記述更新
- [x] M1: Ep15 末尾追記 + word_count 更新
- [x] M2: Ep19 または Ep20 の story_day 修正
- [x] M3 or M7: "Three" の重複解消（どちらか一方）
- [x] M4: Ep48 冒頭にブリッジ文追加
- [x] M5: Ep51 タイトル変更
- [x] M6: Ep59 の General Adelie をキャラクターリストに追加
- [x] M8: Ep76 タイトル変更
- [x] M9: Ep84 の "a long time ago" 修正
- [x] M10: Ep92 / Ep94 タイトル変更
