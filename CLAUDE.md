# Ako-chan's Adventure — Project Instructions

## Key Planning Documents

| File | Purpose |
|------|---------|
| `planning/chapter-design.md` | **全3シーズン確定版チャプター設計（最優先参照）** — 章ごとの柱イベント・確定設計変更・次セッション引き継ぎ |
| `planning/design-decisions.md` | Character settings, world-building, Pod specs, Obia arc, time loop structure |
| `planning/writing-guide.md` | Writing rules, language levels, episode templates, 4-beat structure |
| `planning/s1-episode-list.md` | S1 全話エピソード配置（タイトル・役割） |
| `planning/s2-episode-list.md` | S2 全話エピソード配置（タイトル・役割）— 未作成 |
| `planning/s3-episode-list.md` | S3 全話エピソード配置（タイトル・役割）— 未作成 |
| `planning/s1-episode-outline.md` | ⚠️ 旧版（Riro削除・Pod改称・Obia告白アーク未反映） — 参考のみ |
| `planning/s2-episode-outline.md` | ⚠️ 旧版（同上 + ステラーカイギュウ削除未反映） — 参考のみ |
| `planning/timeline.md` | Day-by-day story events and exact dialogue |
| `_archive/` | 旧S1・S2エピソードおよび旧設定ファイルのアーカイブ（参照用） |

## Writing a New Episode — Required Steps

### Before writing
1. Read `planning/chapter-design.md` の該当チャプターエントリを開き、**柱イベントを確認する**。
2. Read `planning/s1-episode-list.md`（または s2/s3）の該当エピソードエントリを開き、**タイトルと役割を確認する**。
3. Read `planning/s1-episode-outline.md`（または s2）の該当エピソードエントリを開き、**4ビートすべてを確認する**:
   - ①設定、②行動、③補助/テクスチャー、④余韻
   - ⚠️語数確保の指示があれば必ず守る
   - ⚠️旧版のため `chapter-design.md` の設計と矛盾する箇所は `chapter-design.md` を優先する
4. Read `planning/timeline.md` for the relevant chapter/day to confirm:
   - Which `story_day` value to assign
   - What each character already knows at that point in the story
   - Exact wording of any dialogue that later episodes might quote back
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
