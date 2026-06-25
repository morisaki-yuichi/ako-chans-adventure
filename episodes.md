---
layout: default
title: Episodes
permalink: /episodes/
---
{% comment %}
  Chapter numbers are global (Ch1–34): S1 = Ch1–12, S2 = Ch13–24, S3 = Ch25–34.
  Each episode page carries season / chapter / episode in its front matter.
{% endcomment %}
<div class="episodes-page">
  <h1>Episodes</h1>

  <div class="season-block">
    <h2>Season 1 &mdash; A1</h2>

    {% assign s1_titles = "The Voice in the Garden|Following the South|The Turtle on the Rocks|The Red Desert|The Long Way East|Building the Ship|Voices in the Deep|Through the Storm|The White Land|Into the Snow|The Confession|The Way Home" | split: "|" %}
    {% for n in (1..12) %}
    <div class="chapter-block">
      <h3>Chapter {{ n }} &middot; {{ s1_titles[forloop.index0] }}</h3>
      <ul class="episode-list">
        {% assign eps = site.pages | where: "season", 1 | where: "chapter", n | sort: "episode" %}
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
    <h2>Season 2 &mdash; A1&ndash;A2</h2>

    {% assign s2_titles = "The Signal from the South|Building the Flying Boat|Gathering the Friends|South to the Ice|What Obia Remembers|The First Jump|The Island in the Storm|The Rift|Into the Ice Age|Obia's Goodbye|The Long Way Back|Home Without Him" | split: "|" %}
    {% for n in (13..24) %}
    <div class="chapter-block">
      <h3>Chapter {{ n }} &middot; {{ s2_titles[forloop.index0] }}</h3>
      <ul class="episode-list">
        {% assign eps = site.pages | where: "season", 2 | where: "chapter", n | sort: "episode" %}
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
    <h2>Season 3 &mdash; A2&ndash;B1</h2>

    {% assign s3_titles = "The Quiet Years|Gray and Red|The First Words|Reading the Distances|Building Alone|Building Together|Blue-White Light|The Parting|The Ones Who Remember|To the Beginning" | split: "|" %}
    {% for n in (25..34) %}
    <div class="chapter-block">
      <h3>Chapter {{ n }} &middot; {{ s3_titles[forloop.index0] }}</h3>
      <ul class="episode-list">
        {% assign eps = site.pages | where: "season", 3 | where: "chapter", n | sort: "episode" %}
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
