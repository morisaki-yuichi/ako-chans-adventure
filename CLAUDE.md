# Ako-chan's Adventure — Project Instructions

> **⚠️ 2026-07-11 全面再執筆（v2）へ移行済み・本リポジトリは凍結**
> 後継プロジェクト＝ **`~/projects/the-red-notebook`**（The Red Notebook — Ako-chan's Adventure・全277話・非公開で執筆中）。
> 本リポジトリの役割は**公開サイトの現状維持のみ**。本文・計画の新規作業はすべて後継側で行う（確定判断は後継の `planning/decisions.md` が正）。移行の経緯は git log `ecd977d`〜`481e7fd` を参照。

## Key Planning Documents

| File | Purpose |
|------|---------|
| `planning/world.md` | **ワールドバイブル（最優先参照）** — キャラクター設定・Pod仕様・赤い首輪・タイムループ構造 |
| `planning/s1.md` | S1シーズンあらすじ・確定章構成（Ch1〜12・Ep1〜100） |
| `planning/s2.md` | S2シーズンあらすじ・確定章構成（Ch13〜24・Ep101〜200） |
| `planning/s3.md` | S3シーズンあらすじ・確定章構成（Ch25〜34・Ep201〜300） |
| `planning/writing-guide.md` | Writing rules, language levels, episode templates, 4-beat structure |
| `planning/s1-episode-list.md` | S1 全話エピソード配置（タイトル・役割）|
| `planning/s2-episode-list.md` | S2 全話エピソード配置（タイトル・役割）|
| `planning/s3-episode-list.md` | S3 全話エピソード配置（タイトル・役割）|
| `planning/timeline.md` | Day-by-day story events and exact dialogue |
| `planning/continuity-ledger.md` | **内容矛盾を防ぐ3台帳**（A.知識状態・命名／B.配置・動線／C.数・量）— 執筆前に必ず確認 |
| `planning/chapter-workflow.md` | **章マネージャー用プロンプト**（足場準備→執筆プロンプト生成→執筆後レビュー→コミットの一気通貫手順・スキャン集・引き継ぎルール）|

## Writing a New Episode — Required Steps

### Before writing
1. Read `planning/s1.md`（または s2/s3）の章構成を開き、**該当章の柱イベントを確認する**。
2. Read `planning/s1-episode-list.md`（または s2/s3）の該当エピソードエントリを開き、**タイトルと役割を確認する**。
3. Read `planning/timeline.md` for the relevant chapter/day to confirm:
   - Which `story_day` value to assign
   - What each character already knows at that point in the story
   - Exact wording of any dialogue that later episodes might quote back
4. Read `planning/continuity-ledger.md` の3台帳を確認する：その話で**まだ確立していない名前・事実を先取りして呼ばない**（例：名前は確立回まで使わない）・**各キャラの居場所/動線が自然か**・**数え語の確定値**（例：*I have to go.* は4語）。
5. Read `planning/writing-guide.md` Section 9 の執筆プロンプトテンプレートに4ビートを転記してから執筆開始する。

### In the frontmatter
- Set `story_day:` (integer) to the in-story day number.
- If the new episode is on a day not yet in timeline.md, determine the day by counting forward from the last known entry.

### During writing — Mid-draft word count check
- 3段落書いた時点で語数を測定する:
  ```
  awk '/^---/{n++; if(n==2){found=1; next}} found' EPISODE_FILE | wc -w
  ```
  - **230語以下**の場合：③テクスチャービートの段落を追加する
  - **250〜269語**の場合：④余韻を3文以上に拡張する

### After writing or editing an episode
- Add the episode's key facts to `planning/timeline.md` under the correct day:
  - Exact dialogue (especially lines that other episodes may quote)
  - New information characters learn
  - Any time references used ("a few days ago", "yesterday", etc.)
- **Update `word_count:` in the frontmatter** to the actual body word count:
  ```
  awk '/^---/{n++; if(n==2){found=1; next}} found' EPISODE_FILE | wc -w
  ```
  - If below 270: add text before finishing
  - If above 330: trim text before finishing

### After completing a full Chapter
- Propose 3 chapter title candidates based on the chapter's content, and confirm with the user before proceeding.
- **No manual block is needed for episode listing.** The per-season pages (`season1.md` / `season2.md` / `season3.md` → `/season1/` etc.) render chapters data-driven via `_includes/season-list.html`, which loops each chapter and pulls episode pages automatically with `site.pages | where: "season", N | where: "chapter", N | sort: "episode"`. As long as each new episode's frontmatter carries the correct `season` / `chapter` / `episode` / `title` / `word_count`, the chapter renders on its own (as a collapsible `<details>` block). Do **not** hand-write episode lists.
- The only edit ever required is the **chapter title**: confirm the chapter's title is present at the right position in that season's pipe-separated `titles` list **inside `_includes/season-list.html`** (the `if include.season == N` branch). The confirmed S1–S3 titles are already filled in, so normally there is nothing to change.
- **`episodes.md` is now just a season chooser** (it renders `_includes/season-cards.html`) — it carries no episode/chapter list, so never add chapter blocks there. The site entry flow is: home (`index.md`) and `/episodes/` show season cards → each card links to a per-season page.

### Site chrome (navigation / intro copy)
- Top synopsis (`index.md`), season cards (`_includes/season-cards.html`), and per-season intros (`season{1,2,3}.md`) follow the writing-guide grade levels: **entrance (top + cards) = A1**; **each season-page intro = that season's level** (S1 A1 / S2 A2 / S3 B1).
- Keep chrome **spoiler-safe**: do not reveal Obia's name, the journey's direction/destination, the flying boat, the boy's identity, or the red collar. See memory `site-chrome-writing-policy`.
- Custom stylesheet is `assets/css/main.css` (renamed from `style.css` to avoid the implicit `jekyll-theme-primer` `style.css` output collision — do not rename it back). Local preview: see memory `jekyll-local-preview-setup`.

## Critical Continuity Rules

- **The disturbance started when Obia arrived.** No character can say it has been going on longer than Obia has been in this era. Check Obia's arrival date in timeline.md before writing any such reference.
- **Quoted dialogue must match exactly.** When an episode quotes a previous episode's words (e.g., Ep5 recalling Obia's words from Ep3), use the exact text from timeline.md, not from memory.
- **"For a long time" and similar phrases are red flags.** Before using any phrase that implies duration, verify it against Obia's timeline.
