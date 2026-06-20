# Ako-chan's Adventure — Project Instructions

## Key Planning Documents

| File | Purpose |
|------|---------|
| `planning/design-decisions.md` | Character settings, world-building, full season structure |
| `planning/writing-guide.md` | Writing rules, language levels, episode templates |
| `planning/timeline.md` | Day-by-day story events and exact dialogue (start with Chapter 1) |

## Writing a New Episode — Required Steps

### Before writing
1. Read `planning/timeline.md` for the relevant chapter/day to confirm:
   - Which `story_day` value to assign
   - What each character already knows at that point in the story
   - Exact wording of any dialogue that later episodes might quote back
2. Read `planning/design-decisions.md` for the episode's content outline.

### In the frontmatter
- Set `story_day:` (integer) to the in-story day number.
- If the new episode is on a day not yet in timeline.md, determine the day by counting forward from the last known entry.

### After writing
- Add the episode's key facts to `planning/timeline.md` under the correct day:
  - Exact dialogue (especially lines that other episodes may quote)
  - New information characters learn
  - Any time references used ("a few days ago", "yesterday", etc.)

### After completing a full Chapter
- Add a new chapter block to `episodes.md` following the existing pattern:
  ```liquid
  <div class="chapter-block">
    <h3>Chapter N &middot; Ep X–Y</h3>
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
