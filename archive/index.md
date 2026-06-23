---
layout: default
title: Archive — Season 1 & 2 (旧版)
permalink: /archive/
---
<div class="episodes-page">
  <h1>Archive — Season 1 &amp; 2 <small>(旧版)</small></h1>
  <p>These are the original Season 1 and Season 2 episodes. Revised versions are available on the <a href="{{ '/episodes/' | relative_url }}">Episodes</a> page.</p>

  <div class="season-block">
    <h2>Season 1</h2>

    {% assign s1_chapters = site.archive | where: "season", 1 | map: "chapter" | uniq | sort %}
    {% for ch in s1_chapters %}
    <div class="chapter-block">
      <h3>Chapter {{ ch }}</h3>
      <ul class="episode-list">
        {% assign eps = site.archive | where: "season", 1 | where: "chapter", ch | sort: "episode" %}
        {% for ep in eps %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>
    {% endfor %}
  </div>

  <div class="season-block">
    <h2>Season 2</h2>

    {% assign s2_chapters = site.archive | where: "season", 2 | map: "chapter" | uniq | sort %}
    {% for ch in s2_chapters %}
    <div class="chapter-block">
      <h3>Chapter {{ ch }}</h3>
      <ul class="episode-list">
        {% assign eps = site.archive | where: "season", 2 | where: "chapter", ch | sort: "episode" %}
        {% for ep in eps %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>
    {% endfor %}
  </div>
</div>
