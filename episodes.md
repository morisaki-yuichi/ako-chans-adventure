---
layout: default
title: Episodes
permalink: /episodes/
---
<div class="episodes-page">
  <h1>Episodes</h1>

  <div class="season-block">
    <h2>Season 1 &mdash; A1</h2>

    <div class="chapter-block">
      <h3>Chapter 1 &middot; Ep 1–7</h3>
      <ul class="episode-list">
        {% assign s1c1 = site.pages | where: "season", 1 | where: "chapter", 1 | sort: "episode" %}
        {% for ep in s1c1 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

  </div>
</div>
