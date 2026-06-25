# Ako-chan's Adventure — Project Instructions

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
| `_archive/` | 旧S1・S2エピソードおよび旧設定ファイルのアーカイブ（参照用） |

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
- Add a new chapter block to `episodes.md` following the existing pattern:
  ```liquid
  <div class="chapter-block">
    <h3>Chapter N &middot; Chapter Title</h3>
    <ul class="episode-list">
      {% assign s1cN = site.pages | where: "season", 1 | where: "chapter", N | sort: "episode" %}
      {% for ep in s1cN %}
      <li>
        <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
        <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
      </li>
      {% endfor %}
    </ul>
  </div>
  ```

## Critical Continuity Rules

- **The disturbance started when Obia arrived.** No character can say it has been going on longer than Obia has been in this era. Check Obia's arrival date in timeline.md before writing any such reference.
- **Quoted dialogue must match exactly.** When an episode quotes a previous episode's words (e.g., Ep5 recalling Obia's words from Ep3), use the exact text from timeline.md, not from memory.
- **"For a long time" and similar phrases are red flags.** Before using any phrase that implies duration, verify it against Obia's timeline.
