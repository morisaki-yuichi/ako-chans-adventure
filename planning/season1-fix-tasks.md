# Season 1 修正タスクリスト

> 作成日: 2026-06-21  
> 依拠: planning/season1-review.md（全100エピソードレビュー結果）  
> 優先順位: P1（即修正） → P2（次フェーズ） → P3（任意・検討）

---

## P1-S：物語・設定の修正（ストーリー整合性）

---

### TASK-S1 ★★★ Ep100 — Season 2 への引きを強化

**ファイル:** `season1/chapter11/ep100.md`

**問題:**  
現状の最終行「We are not finished.」は静かな力があるが、Season 2 を知らない読者には「何が未解決で、次に何をするのか」が曖昧。Ep99のハリネズミの台詞「The ground still feels wrong. But less. Not as loud.」とEp98のObiaの「Not smaller. But different.」は伏線として機能しているが、その意味（根本原因がまだ氷の下にある）が最終エピソードで回収されていない。

**修正案:**  
Ep100の日記に1〜2文追加し、「南極の氷の下の根本原因はまだそこにある」という事実を読者が持ち帰れるようにする。例:
```
The root is still there. Under the ice. We have not reached it yet.
We are not finished.
```
または、Ep100の中で Ako-chan が Obia に「Is it over?」と問い、Obia が「The pull is smaller. But the root is still there.」と答える1往復を追加する（台詞パターンで処理）。

**注意:** timeline.md の最終行「We are not finished.」は保持したまま前後を補う。追記後、timeline.md も更新する。

---

### TASK-S2 ★★ Ep96・97 — Daru・Gabu の別れシーンを拡充

**ファイル:** `season1/chapter11/ep096.md`, `ep097.md`

**問題:**  
Ep96（Daru との別れ）・Ep97（Gabu との別れ）は各1エピソードで処理されており、Chapter 4–5 で Daru の加入に3エピソード、Gabu の加入に4エピソードを費やしたのと比べて著しく短い。特に Daru はこの旅で最も長く一緒にいた仲間であり、別れのエモーションが薄い。

**修正案（どちらか選ぶ）:**
- A) 各エピソードのワード数を現状の2倍程度に拡充し、別れの情景・Dango の反応・Ako-chan の内面を加える
- B) Daru については Ep96 の前に1エピソード（Ep95.5 相当）を追加し、Daru と最後の夜を過ごすシーンを入れる（この場合 Ep 番号の振り直しが必要）

**優先するアプローチ:** A（既存エピソードの拡充）の方が構造変更なしで対応できる。

**注意:** Dango が Daru・Gabu の別れにどう反応するかも書くこと（嫉妬アークの着地点として機能する可能性）。

---

### TASK-S3 ★★ Ep97 — クロアチア→ヨルダン 帰路の所要日数を確認・修正

**ファイル:** `season1/chapter11/ep097.md`  
**参照:** `planning/timeline.md`

**問題:**  
帰路でクロアチア（Day 95）→ヨルダン（Day 98）= **3日間**。  
往路では Ep30（クロアチア・Day 11）→ Ep31（移動2日）→ Ep33（ヨルダン到着・フェリー5日 = Day 16→33）と、ヨルダン到着まで 20日以上かかっている。  
帰路は経路が異なる可能性があるが、現状 Ep97 にその説明がない。

**修正案（どちらか選ぶ）:**
- A) Ep97 の冒頭 or Ep96 末尾に「Obia took them south by a faster route.」などの1行を追加して説明をつける
- B) Day 98 → Day 101〜103 に変更し、Gabu 到着を3日後ろ倒しにする（この場合 Ep98〜100 の story_day も +3 のシフトが必要。最終 Day は 110 になる）

**推奨:** A（1行の説明追加で整合性を担保）。往路と帰路で「Obia が別ルートを使った」という事実は世界観的に自然。

---

### TASK-S4 ★ Chapter 3（Ep15–20）— 間延び箇所の特定と圧縮

**ファイル:** `season1/chapter03/ep015.md` 〜 `ep020.md`

**問題:**  
山岳の夜行列車 → クロアチア到着の6エピソードが、Chapter 4（Daru 合流）への期待を高めるより「移動時間の消化」になっている。

**修正案:**  
6エピソードを通読して最も内容が薄い1〜2エピソードを特定し、以下のいずれかで対処:
- 台詞・情景を削って読み応えのある要素を前後に移動する
- Ep15–20 のどれかに「Daru からの何か（痕跡・音・噂）」への言及を入れ、期待感を早期に醸成する

**注意:** Chapter 3 は story_day 5–6 で完結しており、日数・継続性は問題ない。純粋に読み感の問題。

---

### TASK-S5 ★ General Adelie のアーク補強（Ep77〜91 の間） ✅ 完了（対応済み）

**ファイル:** 該当する Chapter 9–10 の Ep77〜90 の中の1〜2エピソード（要特定）

**問題:**  
Ep77（大佐登場・「お前たちは期待されていた」）→ Ep91（「ただ働いた。それだけで十分だ。」）の間で、大佐が Obia を認めるに至る心理変化が行動描写だけで示されている。読者によっては Ep91 のセリフが唐突。

**修正案:**  
Chapter 10（Ep81–90）のどこか1箇所で、大佐が Obia の行動を「観察して何かを感じた」という Ako-chan 視点の1段落を追加する。大佐のセリフは不要。「The General watched Obia for a long time. She did not speak. But she did not look away.」程度の1〜2文でよい。

**対応状況（新エピソード番号）:**  
既存の改訂版エピソードがすでに十分カバーしている。追加不要。  
- Ep79: 大佐がObiaを監視、Ako-chanが両者を観察する場面×3  
- Ep84: 「His face was very still. Not angry. Not afraid. Something she could not read.」  
- Ep86: 「But something in the way he held himself was different now.」  
- Ep88: 「He was watching Obia. But not the way he watched before. Something was different. Ako-chan could not say what. She could only see it.」  
→ 新Ep89の「You did not hide it. You just worked. That is enough.」への橋渡し完成。

---

## P1-A：禁止文型の修正（文法ルール違反）

Season 1の禁止文型（分詞構文・関係代名詞節・過去完了形）の違反。読者の理解を直接妨げる。

---

### TASK-01 ★★★ Ep78 — 42語文の分割 + where節除去

**ファイル:** `season1/chapter09/ep078.md`

**問題文:**
```
Pen-san did not stop talking for most of the day, and by the time they stopped walking,
everyone knew his name, his favorite fish, the exact position where he liked to sleep,
and many other things no one had asked about.
```
違反: ①42語（最長違反） ②関係副詞 where 節 ③"no one had asked" = 過去完了相当

**修正案:**
```
Pen-san did not stop talking.
By the time they stopped walking, everyone knew his name.
They knew his favorite fish.
They knew where he liked to sleep.
They knew many other things. No one had asked for any of it.
```
※ where節は残してよいが、文を分割して短くする。"no one had asked about"も単純過去に。

---

### TASK-02 ★★★ Ep72 — 関係代名詞 that 節除去 + 長文2件分割

**ファイル:** `season1/chapter08/ep072.md`

**問題①（関係代名詞）:**
```
a low, deep feeling that came up through the hull and into Ako-chan's feet and hands.
```
→ `a low, deep feeling. It came up through the hull and into Ako-chan's feet and hands.`

**問題②（29語長文）:**
```
The pull from the south was not a pull anymore. It pressed against Ako-chan from all sides
— from the air, from the dark water below, from the white line ahead.
```
→ emダッシュ以降を別文に: `It pressed from the air. From the dark water below. From the white line ahead.`

**問題③（26語長文）:**
```
Their voices were quiet — not words, just a low, deep feeling that came up through the hull
and into Ako-chan's feet and hands.
```
（①と同箇所の別形。①と同時に修正。）

---

### TASK-03 ★★★ Ep66 — 過去完了形の除去

**ファイル:** `season1/chapter08/ep066.md`

**問題文:**
```
much faster than Ako-chan had ever seen them move
```
違反: 過去完了形 `had ever seen`（Season 1禁止）

**修正案:**
```
faster than Ako-chan ever saw them move
```
または
```
They moved faster than anything she knew.
```

---

### TASK-04 ★★★ Ep63・64・68 — 分詞構文の除去（Chapter 8）

**ファイル群:** `season1/chapter08/ep063.md`, `ep064.md`, `ep068.md`

| エピソード | 問題箇所 | 修正案 |
|----------|---------|--------|
| Ep63 | `like something rising from below the world` | `like something that rose from below the world` → さらに簡略化: `It felt like something from below the world.` |
| Ep64 | `Not falling straight down. Going sideways, in sheets.` | `It did not fall straight down. It went sideways, in sheets.` |
| Ep64 | `held fast to the ship` | `She held the ship. She held it fast.` |
| Ep68 | `his head pressed to her knee` | `His head was on her knee.` |

---

### TASK-05 ★★★ Ep74・75・76・79・80 — 分詞構文の除去（Chapter 9–11）

**ファイル群:** `season1/chapter09/ep074.md`, `ep075.md`, `ep076.md`, `ep079.md`, `ep080.md`

| エピソード | 問題箇所 | 修正案 |
|----------|---------|--------|
| Ep74 | `detached now from the ship, rolling slowly on the ice` | `It was detached from the ship now. It rolled slowly on the ice.` |
| Ep75 | `And coming not from animals nearby but from far under the ice, rising up through her feet` | `It did not come from animals nearby. It came from far under the ice. It rose up through her feet.` |
| Ep76 | `rolling from side to side, wings out for balance, feet slapping the ice as fast as they could go.` | `It rolled from side to side. Its wings were out. Its feet slapped the ice as fast as they could go.` |
| Ep79 | `on the night train, many weeks ago, crossing into Croatia` | `on the night train, many weeks ago, when they crossed into Croatia` → さらに単純化: `on the night train many weeks ago. That was when they crossed into Croatia.` |
| Ep80 | `like something breathing` | `like something that breathed` → `like a living thing` |
| Ep80 | `face pressed to the glass` | `Her face was against the glass.` |
| Ep80 | `door open a little` | `The door was open a little.` |

---

## P1-B：A1超過語彙の置換（頻出・影響大）

---

### TASK-06 ★★★ enormous の置換（Chapter 9 中心） ✅ 完了（修正不要）

**登場箇所:** Ep73, Ep74, Ep75, Ep76, Ep77 以降（6回以上）

`enormous` は NGSL 上位 1000 語外 (B1)。

**代替候補:** `very big` / `very large`  
※ ただし "an enormous whale" のような種類描写では、韻律・語感を考慮して判断。

各エピソードの用例を確認して、文脈に合う代替語を選ぶこと。

---

### TASK-07 ★★★ exhausted・urgency・pulse の置換 ✅ 完了（修正不要）

**登場箇所:**

| 語 | エピソード | 代替案 |
|----|----------|--------|
| exhausted | Ep68 | `very tired` |
| urgency | Ep68, Ep80 | `hurry` / `something pushing her` / 副詞的表現に変換 |
| pulse | Ep75, Ep79, Ep80 | `beat` / `feeling` / `sound` |

**Ep68 の urgency の文脈例:**
> There was an urgency in it.

→ `It felt like hurry.` / `It pushed her forward.`

---

## P2-A：長文の分割（12語超）

文型ルール違反ではないが、A1の「1文12語以内（最大でも12語）」基準を超えるもの。

---

### TASK-08 ★★ 長文修正 — Ep33・44・48・53・55（Chapter 5–7）

| Ep | 問題文（冒頭） | 語数 | 修正方針 |
|----|-------------|------|---------|
| Ep33 | `The heat came from above and below and from the red walls on both sides, all at the same time.` | 19語 | `The heat came from above. From below. From the red walls on both sides.` |
| Ep44 | `Then there was just the dark sea and the dark sky and the low sound of the engine below their feet.` | 21語 | 接続詞 and を減らして短文へ分割 |
| Ep48 | `Then it looked at the others: Daru in the pod, Gabu very still at the edge of the camp, Dango standing just in front of Ako-chan.` | 27語 | コロン以降を別文化し、分詞構文「standing」も除去 |
| Ep53 | `It came from below the water and moved up through the hull and into her feet and then into her whole body.` | 21語 | `It came from below the water. It moved up through the hull. It reached her feet. Then her whole body.` |
| Ep55 | `This was the thing about Suke-san and Dango on the ship: the deck was not large, and they both wanted to be near Ako-chan.` | 25語 | コロンで2文に分け、さらに分割 |

---

### TASK-09 ★★ 長文修正 — Ep76・79（Chapter 9）

| Ep | 問題文（冒頭） | 語数 | 修正方針 |
|----|-------------|------|---------|
| Ep76 | `It came across the ice at full speed, rolling from side to side, wings out for balance, feet slapping the ice as fast as they could go.` | 27語 | TASK-05と同時修正（分詞構文除去で自動的に分割） |
| Ep79 | `The sky above was dark and full of stars — more stars than she ever saw at home, and brighter, so bright they did not look real.` | 26語 | emダッシュで分割: `The sky above was dark and full of stars. There were more stars than she ever saw at home. They were brighter. So bright they did not look real.` |

---

## P2-B：設定・継続性の修正

---

### TASK-10 ★★ Ep61 — Obiaの台詞に1行追加

**ファイル:** `season1/chapter07/ep061.md`

**現状のObia台詞:**
```
Get in. The ship will carry you. When we reach the equator, this will keep you cool.
```

**timeline.md の正典:**
```
Get in. The ship will carry you. You do not need to swim. And when we reach the equator — this will keep you cool.
```

`You do not need to swim.` を追加し、`And` と emダッシュを補う。

---

### TASK-11 ★ Ep38 — Gabuの「約15日前」タイムライン注記

**ファイル:** `season1/chapter05/ep038.md`  
**参照:** `planning/timeline.md`

**状況:**  
Gabuが story_day 19 の時点で「約15日前（Day 4）に変化が始まった」と言う。  
DaruはDay 8の時点で「約8日前（Day 0）」と言っており、Obiaの到着（Day -2）と2日のズレがある。  
クロアチア（北）よりもヨルダン（南）の方が異変の発症が遅いのは、「南に近いほど異変が強い」設定と整合しない可能性がある。

**対応方針（検討）:**  
① Ep38のGabuの台詞を「約10日前」に変更（Day 9 → Obiaの到着（Day -2）から11日後 → クロアチアとほぼ同時期）  
② または timeline.md に「砂漠の動物は異変を感じるのが遅れた」という注記を追加し、将来の言及に備える  
③ 現状維持（大きな問題ではないと判断）

---

## P3：低優先度・方針決定が必要なもの

---

### TASK-12 ★ hull の扱い方針を決定 ✅ 完了（初出補強、以降はそのまま）

**登場箇所:** Ep44, Ep52, Ep53, Ep62, Ep67, Ep72（複数）→ 新番号: Ep42, Ep50, Ep51, Ep60, Ep65, Ep70

`hull`（船体）は B1/B2 レベルだが、物語の重要なモチーフ（「船体から振動が伝わる」感覚）として繰り返し使われる。

**選択肢:**
- A) `hull` → `the ship` で統一（意味は変わらない）
- B) 初出（Ep44 or Ep52）で1回だけ説明的に使い、以降は `the ship` に
- C) 物語の専門用語として許容し、Glossary/語注に追加

**対応:** Ep42（初出）の「I can feel it in the hull.」の直後に3文追加：  
> The hull. The body of the ship. It sat deep in the water below them.  
以降の登場（Ep50, Ep51, Ep60, Ep65, Ep70 等）はそのまま使用。

---

### TASK-13 ★ disturbance の扱い方針を決定 ✅ 完了（選択肢B）

**登場箇所:** Ep25, Ep42, Ep80, Ep85, Ep89 等（複数）→ 新番号: Ep22, Ep40, Ep78, Ep83, Ep87

物語の中核概念語。B1レベルだが、「異変」を表す最適な英単語として機能している。

**選択肢:**
- A) `the wrong thing` / `the bad thing` / `it` に置き換え（A1準拠）
- **B) 物語の鍵語として許容し、初出時にコンテクストで意味を取れるよう周辺文を補強 ← 採用**
- C) Season 1では `something wrong` 等で通し、Season 2以降で `disturbance` を導入

**対応:** Ep22（初出）の「"You felt it," said Ako-chan. "The disturbance. From the south."」の直前に3文追加：  
> Something was wrong in the south. Ako-chan knew it. She heard it in the animals' voices all the way from England.  
以降の登場（Ep40, Ep78, Ep83, Ep87）はそのまま使用。

---

### TASK-14 ★ イギリス英語固有語の方針決定 ✅ 完了（イギリス英語維持）

**対象語と登場箇所:**

| 英国語 | 米国語 | エピソード |
|-------|-------|----------|
| torch | flashlight | Ep6 |
| jumper | sweater | Ep6 |
| lead（リード） | leash | Ep7 |

日本人英語学習者に普及しているのは米国英語が多い。シリーズとしてどちらに統一するか（または「Ako-chanはイギリス在住」という設定を生かして英国語を維持するか）を決める。

**対応:** Ako-chanはイギリス在住という設定を生かし、イギリス英語をそのまま維持。修正不要。

---

### TASK-15 ★ 中頻度上級語の置換（単発・文脈で補える語）

以下は単発または少数登場で、文脈から意味が取れるものが多い。改訂の機会があれば対処。

| 語 | Ep | 代替案 |
|----|---|--------|
| jutting | 33 | `stuck out` |
| panting | 33, 34 | `breathing hard` / `breathing fast` |
| snout | 34 | `nose` |
| ledge | 35 | `flat rock shelf` |
| swells | 43, 55 | `big waves` |
| bow（船首） | 54 | `the front of the ship` |
| afloat | 56 | `on the water` |
| gaze | 47 | `look` / `eyes` |
| systematic | 58 | `very careful` |
| clearing | 46 | `open place in the forest` |
| compact | 49 | `small and strong` |
| waddled | 80 | `walked from side to side` |
| faded | 74 | `went away` |
| dim | 79 | `almost dark` |
| gripped | 72 | `held hard` |
| blur | 69 | `not clear` |
| precise | 77 | `very careful. Very exact.` |

---

## 修正優先度サマリー

| タスク | 優先度 | 種別 | 対象Ep |
|--------|--------|------|-------|
| TASK-S1 | ★★★ P1 | 物語（Season 2 への引き強化） | Ep100 |
| TASK-01 | ★★★ P1 | 文法（42語文+関係節） | Ep78 |
| TASK-02 | ★★★ P1 | 文法（関係節+長文） | Ep72 |
| TASK-03 | ★★★ P1 | 文法（過去完了） | Ep66 |
| TASK-04 | ★★★ P1 | 文法（分詞構文） | Ep63, 64, 68 |
| TASK-05 | ★★★ P1 | 文法（分詞構文） | Ep74, 75, 76, 79, 80 |
| TASK-06 | ★★★ P1 | 語彙（enormous） | Ep73–80 |
| TASK-07 | ★★★ P1 | 語彙（exhausted等） | Ep68, 75, 79, 80 |
| TASK-S2 | ★★ P2 | 物語（別れシーン拡充） | Ep96, 97 |
| TASK-S3 | ★★ P2 | 継続性（帰路日数） | Ep97 |
| TASK-08 | ★★ P2 | 長文分割 | Ep33, 44, 48, 53, 55 |
| TASK-09 | ★★ P2 | 長文分割 | Ep76, 79 |
| TASK-10 | ★★ P2 | 継続性（台詞修正） | Ep61 |
| TASK-11 | ★★ P2 | 継続性（タイムライン検討） | Ep38 |
| TASK-S4 | ★ P3 | 物語（Chapter 3 圧縮） | Ep15–20 |
| TASK-S5 | ★ P3 | 物語（Adelie アーク補強） | Ep77–90 |
| TASK-12 | ★ P3 | 方針決定（hull） | 複数Ep |
| TASK-13 | ★ P3 | 方針決定（disturbance） | 複数Ep |
| TASK-14 | ★ P3 | 方針決定（英国英語） | Ep6, 7 |
| TASK-15 | ★ P3 | 語彙（単発上級語） | 各所 |
