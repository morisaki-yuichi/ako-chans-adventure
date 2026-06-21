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

    <div class="chapter-block">
      <h3>Chapter 4 &middot; The Curious One</h3>
      <ul class="episode-list">
        {% assign s1c4 = site.pages | where: "season", 1 | where: "chapter", 4 | sort: "episode" %}
        {% for ep in s1c4 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="chapter-block">
      <h3>Chapter 5 &middot; The Patient One</h3>
      <ul class="episode-list">
        {% assign s1c5 = site.pages | where: "season", 1 | where: "chapter", 5 | sort: "episode" %}
        {% for ep in s1c5 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="chapter-block">
      <h3>Chapter 6 &middot; The Watchful One</h3>
      <ul class="episode-list">
        {% assign s1c6 = site.pages | where: "season", 1 | where: "chapter", 6 | sort: "episode" %}
        {% for ep in s1c6 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="chapter-block">
      <h3>Chapter 7 &middot; The Voice of the Whales</h3>
      <ul class="episode-list">
        {% assign s1c7 = site.pages | where: "season", 1 | where: "chapter", 7 | sort: "episode" %}
        {% for ep in s1c7 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="chapter-block">
      <h3>Chapter 8 &middot; Into the Storm</h3>
      <ul class="episode-list">
        {% assign s1c8 = site.pages | where: "season", 1 | where: "chapter", 8 | sort: "episode" %}
        {% for ep in s1c8 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="chapter-block">
      <h3>Chapter 9 &middot; At the End of the South</h3>
      <ul class="episode-list">
        {% assign s1c9 = site.pages | where: "season", 1 | where: "chapter", 9 | sort: "episode" %}
        {% for ep in s1c9 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="chapter-block">
      <h3>Chapter 10 &middot; The Root of It</h3>
      <ul class="episode-list">
        {% assign s1c10 = site.pages | where: "season", 1 | where: "chapter", 10 | sort: "episode" %}
        {% for ep in s1c10 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

  </div>
</div>
