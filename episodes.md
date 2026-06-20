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
      <h3>Chapter 1 &middot; The Voices in the Garden</h3>
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

    <div class="chapter-block">
      <h3>Chapter 2 &middot; South by Rail</h3>
      <ul class="episode-list">
        {% assign s1c2 = site.pages | where: "season", 1 | where: "chapter", 2 | sort: "episode" %}
        {% for ep in s1c2 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="chapter-block">
      <h3>Chapter 3 &middot; A Small Light</h3>
      <ul class="episode-list">
        {% assign s1c3 = site.pages | where: "season", 1 | where: "chapter", 3 | sort: "episode" %}
        {% for ep in s1c3 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

  </div>
</div>
