# Season 2 Review — Full Report

Reviewed: 2026-06-23  
Scope: All 100 episodes (Chapter 12–22), cross-checked against design-decisions.md, writing-guide.md, timeline.md

Sub-reports (kept for detail):
- `planning/season2-review-ch12-15.md` (Ep1–30)
- `planning/season2-review-ch16-18.md` (Ep31–60)
- `planning/season2-review-ch19-22.md` (Ep61–100)

---

## 1. 物語の展開 (Story Development)

全体として、Season 2 の物語構造は一貫しており流れもよい。各チャプターに明確な役割がある。

| Chapter | 役割 | 評価 |
|---------|------|------|
| Ch12 (Ep1–7) | 日常への帰還・Ruka 紹介 | ✓ 自然な導入 |
| Ch13 (Ep8–14) | 謎の信号・Obia の locked memory | ✓ テンポよく緊張感を積む |
| Ch14 (Ep15–20) | 飛行艇建造 (14日間) | △ 6話で大きな動きが少ない。Ep16とEp17は統合も検討できる |
| Ch15 (Ep21–30) | 旅立ち・クロアチア・ヨルダン (Daru / Gabu 合流) | ✓ 感情的にも満足度が高い |
| Ch16 (Ep31–39) | 日本・北太平洋 (Suke-san / Riro 合流) | ✓ 一つひとつの再会が丁寧に描かれている |
| Ch17 (Ep40–50) | 南極接近・Pen-san / General Adelie 再会 | ✓ 感情的ピーク |
| Ch18 (Ep51–60) | タイムマシン発見・Obia の記憶解放・ミッション判明 | ✓ 慎重で的確なペース |
| Ch19 (Ep61–70) | 時間旅行1〜3回目 (日本・北大西洋・ベーリング海) | ✓ 各ジャンプが自己完結したミニアーク |
| Ch20 (Ep71–80) | Ice Age の事故・Meiolania との遭遇 | ✓ 最も感情的に複雑なアーク |
| Ch21 (Ep81–90) | 帰還・ミッション完了・Obia の別れへの準備 | ✓ 丁寧に感情を積み上げ |
| Ch22 (Ep91–100) | Obia との別れ・England への帰路・Season 3 への橋渡し | ✓ 抑制的で余韻があるフィナーレ |

**懸念点:**
- Ch14 (Ep15–20): 飛行艇建造に6エピ使うが、大きなドラマが少なく読者が飽きる可能性がある。エラーではないが構造上の弱点。
- Day 40 が Ep44–60 (17エピ) にわたる点は内容的には正当化できるが、テキスト内に時間的な目印がEp44の "By morning" 以降ない。
- Day 41 が Ep61–82 (22エピ) にわたるのは時間旅行の設定上正当だが、テキスト内で明示されていない。

---

## 2. 設定の整合性 (Setting Consistency)

### 重大な不整合

| 優先度 | Ep | 内容 |
|--------|-----|------|
| HIGH | Ep2 | Ruka の合流を "just a few weeks ago" と書いているが、design-decisions.md・timeline.md はどちらも「Season 2 開幕の約1年前」と明記している |
| HIGH | timeline.md | Ep97 の記述 (line 2318) が旧バージョンのまま。Pen-san と General Adelie が飛行艇に乗っているとなっているが、commit 5e24863 で修正済みのエピソードは二人を南極に残している |

### 軽微な不整合

| 優先度 | Ep | 内容 |
|--------|-----|------|
| MEDIUM | Ep84 | "The hedgehog said so. A long time ago." — S1 最終章の出来事を指しているが、「a long time ago」は曖昧で、S2 以前の出来事と分からない読者が混乱する可能性がある |
| LOW | Ep21 | Ruka のスペースを "soft orange light" と描写しているが、design-decisions.md では Ruka の発光色は「黄色」。また "orange" は Gabu のポッドの色と混同される |
| LOW | Ep40 | Obia がポッドを「2つ積んで運んできた」あとに「最後のもの (黄色のポッド)」を出す描写で、運搬が2往復なのか1回なのか不明確 |
| LOW | Ep59 | Ako-chan が動物たちを一人ずつ見る場面で General Adelie がリストから抜けているが、直後に発言する |

### 良好な整合性 (representative)
- Obia の inner light (S1 Ep16/77 → S2 Ep12) ✓
- General Adelie の称号: Ako-chan の記憶では "the Colonel"、Ep49 で "General" に訂正 ✓
- ハリネズミの "the ground is quiet" (S1 解決に整合) ✓
- Gabu の3歩止まりパターン、Daru の一直線走り ✓
- Ruka の pod 入り (Ep44 で自発的) ✓
- 各再会セリフが timeline.md と完全一致 ✓
- Ep97 の Pen-san / General Adelie を南極に残す修正が Ep91–96 のポッド描写と整合 ✓

---

## 3. エピソードタイトル (Titles)

### Season 2 内の重複タイトル（全件）

| タイトル | Ep (Season 2) | 内容 | 優先度 |
|----------|---------------|------|--------|
| "East" | Ep21 (Ch15) / Ep31 (Ch16) | Ep21=英国出発・東へ / Ep31=日本へ向かう | **HIGH** |
| "Hands" | Ep17 (Ch14) / Ep94 (Ch22) | Ep17=飛行艇建造シーン / Ep94=Obia への最後の別れ | **HIGH** |
| "Three" | Ep30 (Ch15) / Ep70 (Ch19) | Ep30=カメ3頭 / Ep70=3回目の揺れ | MEDIUM |
| "Suke-san" | Ep34 (Ch16) / Ep92 (Ch22) | Ep34=Suke-san 合流 / Ep92=Suke-san の別れ | MEDIUM |
| "Still" | Ep76 (Ch20) / Ep98 (Ch22) | Ep76=Meiolania と対峙 / Ep98=英国帰還・静けさ | MEDIUM |

**改名候補:**

| 変更対象 | 現タイトル | 候補 |
|----------|-----------|------|
| Ep17 | "Hands" | "Hold" / "The Join" / "Together" |
| Ep21 | "East" | "Lift" / "Above England" / "Rising" |
| Ep31 | "East" | "One More Day" / "To Japan" |
| Ep30 | "Three" | "Three Tortoises" / "We Go East" |
| Ep70 | "Three" | "The Third" / "Three Times" / "Harder" |
| Ep34 | "Suke-san" | 内容を確認して検討（Gabu 合流の回か確認） |
| Ep92 | "Suke-san" | "The Bow" / "His Answer" |
| Ep76 | "Still" | "Waiting" / "Recognition" / "Forty Seconds" |
| Ep94 | "Hands" | "Her Hand" / "Farewell" / "On His Head" |

注: "Voices" (Ep79) と "Four Voices" (Ep82) は重複ではなく、意図的な関連として問題なし。

### タイトルと内容の不一致

| Ep | タイトル | 問題 | 候補 |
|----|----------|------|------|
| Ep51 | "Across" | 横断ではなく洞窟の奥に向かう場面で "Across" は不適切 | "Deeper" / "Forward" / "Inward" |

---

## 4. テキストの自然さ (Text Naturalness)

### 語数上限オーバー

| Ep | 語数 | 上限 | 問題 |
|----|------|------|------|
| Ep37 | 344 | 330 | **14〜20語のトリミングが必要** |
| Ep87 | 307 | 330 | 上限内だが末尾段落がやや added-feeling |
| Ep99 | 323 | 330 | ギリギリ上限内、問題なし |

### 語数が少なく唐突に終わる

| Ep | 語数 | 問題 |
|----|------|------|
| Ep15 | 272 | "Yes. This will do." で終わり、閉じるビートがない。10〜20語の追記が必要 |

### トランジション不足

| 箇所 | 問題 | 修正案 |
|------|------|--------|
| Ep47→Ep48 | Ep47 は全員静止で終わる。Ep48 は "They went deeper" で始まる。橋渡し文がない | Ep48 冒頭に "After a long moment, they moved on." 等を追加 |

### 不自然な文・表現

| Ep | 文 | 問題 | 修正案 |
|----|-----|------|--------|
| Ep53 | "Something this shape did not belong here." | 文法的に不自然 | "A shape like this did not belong here." |
| Ep63 | "Something older than those words" | 同一エピ内で2回繰り返し | 一方を削除か言い換え |
| Ep63 | "She let herself be looked at." | 受動的な表現が不自然 | "She held still and let the wolf see her." |
| Ep64 | "She walked with only what was honest." | A2 には抽象的すぎる | "She walked slowly. She had nothing to hide." |

---

## 5. 日数カウント (Day Count)

### 全体の story_day の流れ

| story_day | エピソード | 日数ギャップ | 説明あり？ |
|-----------|---------|------------|----------|
| 1 | Ep1, Ep2 | — | ✓ |
| 2–5 | Ep3–7 | 毎日+1 | ✓ |
| 6–8 | Ep8–12 | 毎日+1 | ✓ |
| 11 | Ep13, Ep14 | +3 | ✓ (エピタイトル "Three Days"、冒頭で説明) |
| 12 | Ep15 | +1 | ✓ |
| 14 | Ep16 | +2 | ✓ ("Two nights later") |
| 17 | Ep17 | +3 | ✓ ("fifth day" of build) |
| 20 | Ep18 | +3 | ✓ ("Three days later") |
| 23 | Ep19 | +3 | ✓ ("Three days later") |
| **26** | **Ep20** | **+3** | **⚠ 不一致: Ep19 で "two more days" = Day 25 のはずが Day 26** |
| 27–31 | Ep21–30 | 毎日+1 | ✓ |
| 32–37 | Ep31–39 | 毎日+1 | ✓ |
| 38–39 | Ep40–43 | +1 ずつ | ✓ |
| **40** | **Ep44–60** | **17エピが同日** | 内容的には数時間の出来事だが、テキスト内に時間の目安がEp44以降ない |
| **41** | **Ep61–82** | **22エピが同日** | 時間旅行の設定上正当だが、テキスト内で未説明 |
| 42 | Ep83–86 | +1 | ✓ |
| 43 | Ep87–88 | +1 | ✓ |
| 44 | Ep89–96 | +1 | ✓ |
| 45 | Ep97 | +1 | ✓ |
| **50** | **Ep98** | **+5** | "Days passed." で処理 — 許容範囲 |

### 確認された不整合

**Ep19→Ep20 の1日ズレ (MEDIUM 優先度)**  
Ep19 で Obia が "two more days" と言う → Day 23 + 2 = **Day 25** のはずだが、Ep20 の story_day は **26**。  
修正案: Ep19 の "two more days" を "three more days" に変更するか、Ep20 の story_day を 25 に変更。

---

## 6. 英語の難易度 (English Difficulty)

### 過去完了 (past perfect) の多用 — シリーズレベルの決定が必要

writing-guide.md では Season 2 の許容時制を present, past, present progressive, will, can/could としており、past perfect は明示的に禁止。しかし Chapter 19 以降で頻繁に使われている。

**検出箇所 (代表例):**
- Ep8: "All of them had felt the same thing." → "felt"
- Ep61: "Japan, Obia had said, before they came through."
- Ep68: "She had been on open seas before."
- Ep73: "She had never seen him move that fast."
- Ep81: "Four animals who had been gone from the world for a very long time."
- Ep84: "She had known something was not finished."
- Ep89: "He had watched Obia since the first night in Antarctica."
- Ep98: "She had felt it for so long."

**決定事項**: writing-guide.md を更新して S2 での限定的な past perfect を許可するか、全インスタンスを単純過去に書き直すか。

### 個別の語彙・表現

| Ep | 語句 | 問題 | 修正案 |
|----|------|------|--------|
| Ep13 | "on purpose" | イディオム | "not by accident" |
| Ep15 | "Measurements" | 5音節、やや難 | "numbers" |
| Ep18 | "As if it was adding something to what it knew" | イディオム的 | 平易な言い換えを検討 |
| Ep25 | 複雑な比較節 "the same way he had grown" | A2 上限 | 任意で簡略化 |
| Ep38 | "satisfied" | A2+、NGSL 上位1000外 | "pleased" または書き換え |
| Ep42 | "descend" | A2 | "go down" (既にEp42でも使用) |
| Ep45 | "ridges" | NGSL 外 | "bumps" / "rises" |
| Ep53 | "flowed" (空間的比喩) | 比喩的用法は A2+ | "moved into" |
| Ep53 | "untouched" | A2+ | "still perfect" |
| Ep67 | "straining" | やや難 | "struggling" |
| Ep75/76 | "ancient" | A2 範囲内だが境界線 | 必要に応じて置換 |
| Ep76 | "recognition" | 抽象名詞 | "It looked at them as if it knew what they were." |
| Ep84–90 | "connection" | 技術用語として反復 — OK | 変更不要 |
| Ep99 | "vanishing" | Obia の発言として定着 — OK | 変更不要 |

### 複雑な関係節

| Ep | 文 | 修正案 |
|----|-----|--------|
| Ep73 | "Gabu, who never moved before thinking, who had always watched and waited and counted — was already at the edge of the crack." | 2文に分割 |
| Ep76 | "As if this creature — which had never seen a tortoise as small as them, from times it would never know — still understood what they were." | 「This creature had never seen a tortoise as small as them. It had come from a time they would never know. But it still understood what they were.」に分割 |

---

## 7. 全体評価

Season 2 は Season 1 の世界観・キャラクター設定を忠実に引き継ぎ、時間旅行という新要素を加えながらも A1-A2 の語彙レベルを概ね維持している。物語の展開は一貫しており、Obia との別れを軸にした感情的な後半は特によく書けている。

主要な修正課題は:
1. **タイトル重複** (5件、全て Season 2 内)
2. **Ruka の合流時期の誤記** (Ep2)
3. **Ep37 の語数上限超過**
4. **past perfect の扱いに関するシリーズレベルの判断**
5. **timeline.md の Ep97 記述の更新**

これらを修正すれば、Season 2 は高品質な多読教材として完成度が高い。
