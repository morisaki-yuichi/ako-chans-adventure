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

    <div class="chapter-block">
      <h3>Chapter 11 &middot; All the Way Home</h3>
      <ul class="episode-list">
        {% assign s1c11 = site.pages | where: "season", 1 | where: "chapter", 11 | sort: "episode" %}
        {% for ep in s1c11 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

  </div>

  <div class="season-block">
    <h2>Season 2 &mdash; A1&ndash;A2</h2>

    <div class="chapter-block">
      <h3>Chapter 12 &middot; A New Small Thing</h3>
      <ul class="episode-list">
        {% assign s2c12 = site.pages | where: "season", 2 | where: "chapter", 12 | sort: "episode" %}
        {% for ep in s2c12 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="chapter-block">
      <h3>Chapter 13 &middot; A Door That Will Not Open</h3>
      <ul class="episode-list">
        {% assign s2c13 = site.pages | where: "season", 2 | where: "chapter", 13 | sort: "episode" %}
        {% for ep in s2c13 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="chapter-block">
      <h3>Chapter 14 &middot; The Flying Boat</h3>
      <ul class="episode-list">
        {% assign s2c14 = site.pages | where: "season", 2 | where: "chapter", 14 | sort: "episode" %}
        {% for ep in s2c14 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="chapter-block">
      <h3>Chapter 15 &middot; Three Tortoises</h3>
      <ul class="episode-list">
        {% assign s2c15 = site.pages | where: "season", 2 | where: "chapter", 15 | sort: "episode" %}
        {% for ep in s2c15 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="chapter-block">
      <h3>Chapter 16 &middot; Eight</h3>
      <ul class="episode-list">
        {% assign s2c16 = site.pages | where: "season", 2 | where: "chapter", 16 | sort: "episode" %}
        {% for ep in s2c16 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="chapter-block">
      <h3>Chapter 17 &middot; The Ice Below</h3>
      <ul class="episode-list">
        {% assign s2c17 = site.pages | where: "season", 2 | where: "chapter", 17 | sort: "episode" %}
        {% for ep in s2c17 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="chapter-block">
      <h3>Chapter 18 &middot; Save the Voices</h3>
      <ul class="episode-list">
        {% assign s2c18 = site.pages | where: "season", 2 | where: "chapter", 18 | sort: "episode" %}
        {% for ep in s2c18 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="chapter-block">
      <h3>Chapter 19 &middot; Before They Were Gone</h3>
      <ul class="episode-list">
        {% assign s2c19 = site.pages | where: "season", 2 | where: "chapter", 19 | sort: "episode" %}
        {% for ep in s2c19 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="chapter-block">
      <h3>Chapter 20 &middot; The Oldest Ground</h3>
      <ul class="episode-list">
        {% assign s2c20 = site.pages | where: "season", 2 | where: "chapter", 20 | sort: "episode" %}
        {% for ep in s2c20 %}
        <li>
          <a href="{{ ep.url | relative_url }}">Ep {{ ep.episode }} &mdash; {{ ep.title }}</a>
          <span class="ep-tags">{{ ep.level }} &middot; {{ ep.word_count }} words</span>
        </li>
        {% endfor %}
      </ul>
    </div>

  </div>
</div>
