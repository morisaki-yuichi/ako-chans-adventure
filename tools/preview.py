#!/usr/bin/env python3
"""
No-install local previewer for the Ako-chan's Adventure Jekyll site.

Renders episode Markdown files through the real _layouts + assets/css so you can
review pages exactly as GitHub Pages would show them — without Ruby/Jekyll.

Usage:
    python3 tools/preview.py [DIR ...]      # default: season1 season2 season3
    cd _preview && python3 -m http.server 4000
    open http://localhost:4000/

Handles the small Liquid subset used by the layouts:
  {{ page.X }} {{ site.title }} {{ content }}
  {{ '/path' | relative_url }} {{ page.var | relative_url }}
  {% if page.X %}...{% endif %}
Markdown: blank-line paragraphs, **strong**, *em*. (Episodes are plain prose.)
"""
import os, re, sys, shutil, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_preview")
BASEURL = ""  # local preview serves from root


def read_config_title():
    try:
        with open(os.path.join(ROOT, "_config.yml"), encoding="utf-8") as f:
            for line in f:
                m = re.match(r'\s*title:\s*"?(.*?)"?\s*$', line)
                if m:
                    return m.group(1)
    except FileNotFoundError:
        pass
    return "Ako-chan's Adventure"


SITE_TITLE = read_config_title()


def split_frontmatter(text):
    """Return (frontmatter_dict, body). Frontmatter is simple key: value."""
    fm, body = {}, text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].splitlines():
                m = re.match(r'\s*([A-Za-z0-9_]+):\s*(.*)\s*$', line)
                if m:
                    k, v = m.group(1), m.group(2).strip()
                    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                        v = v[1:-1]
                    fm[k] = v
            body = parts[2]
    return fm, body.lstrip("\n")


def md_to_html(body):
    blocks = re.split(r'\n\s*\n', body.strip())
    out = []
    for b in blocks:
        b = b.strip()
        if not b:
            continue
        b = html.escape(b, quote=False)
        b = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', b)
        b = re.sub(r'\*(.+?)\*', r'<em>\1</em>', b)
        b = b.replace("\n", " ")
        out.append(f"<p>{b}</p>")
    return "\n".join(out)


def strip_layout_frontmatter(text):
    _, body = split_frontmatter(text)
    return body


def render_liquid(tpl, page, content):
    s = tpl
    # {% if page.X %}...{% endif %}  (no else)
    def if_repl(m):
        key, inner = m.group(1), m.group(2)
        return inner if page.get(key) else ""
    s = re.sub(r'\{%\s*if\s+page\.([A-Za-z0-9_]+)\s*%\}(.*?)\{%\s*endif\s*%\}',
               if_repl, s, flags=re.S)
    # {{ '...'|relative_url }} and {{ page.var|relative_url }}
    def relurl(m):
        tok = m.group(1).strip()
        if tok.startswith(("'", '"')):
            val = tok[1:-1]
        else:
            val = page.get(tok.replace("page.", ""), "")
        if val and not val.startswith("/"):
            val = "/" + val
        return BASEURL + val
    s = re.sub(r"\{\{\s*(.+?)\s*\|\s*relative_url\s*\}\}", relurl, s)
    # {{ content }}
    s = s.replace("{{ content }}", content)
    # {% if page.title %}...{% endif %} already handled; {{ site.title }}
    s = s.replace("{{ site.title }}", html.escape(SITE_TITLE))
    # {{ page.X }}
    def pagevar(m):
        return html.escape(str(page.get(m.group(1), "")))
    s = re.sub(r"\{\{\s*page\.([A-Za-z0-9_]+)\s*\}\}", pagevar, s)
    return s


def main():
    dirs = sys.argv[1:] or ["season1", "season2", "season3"]
    ep_layout = strip_layout_frontmatter(
        open(os.path.join(ROOT, "_layouts/episode.html"), encoding="utf-8").read())
    def_layout = strip_layout_frontmatter(
        open(os.path.join(ROOT, "_layouts/default.html"), encoding="utf-8").read())

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT, exist_ok=True)
    # assets
    src_assets = os.path.join(ROOT, "assets")
    if os.path.isdir(src_assets):
        shutil.copytree(src_assets, os.path.join(OUT, "assets"))

    episodes = []
    for d in dirs:
        base = os.path.join(ROOT, d)
        if not os.path.isdir(base):
            continue
        for dp, _, files in os.walk(base):
            for fn in sorted(files):
                if not fn.endswith(".md"):
                    continue
                fm, body = split_frontmatter(
                    open(os.path.join(dp, fn), encoding="utf-8").read())
                if "episode" not in fm:
                    continue
                content = md_to_html(body)
                inner = render_liquid(ep_layout, fm, content)
                page_html = render_liquid(def_layout, fm, inner)
                permalink = fm.get("permalink") or f"/{d}/ep{int(fm['episode']):03d}/"
                rel = permalink.strip("/")
                dest = os.path.join(OUT, rel, "index.html")
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "w", encoding="utf-8") as f:
                    f.write(page_html)
                episodes.append(fm)

    # listing (home + /episodes/)
    episodes.sort(key=lambda e: (int(e.get("season", 0)),
                                 int(e.get("chapter", 0)),
                                 int(e.get("episode", 0))))
    items = []
    cur = None
    for e in episodes:
        sc = (e.get("season"), e.get("chapter"))
        if sc != cur:
            if cur is not None:
                items.append("</ul>")
            items.append(f"<h3>Season {e.get('season')} &middot; Chapter {e.get('chapter')}</h3><ul>")
            cur = sc
        link = (e.get("permalink") or "").rstrip("/") + "/"
        items.append(
            f'<li><a href="{link}">Ep {e.get("episode")} &mdash; {html.escape(e.get("title",""))}</a>'
            f' <small>{e.get("level","")} &middot; {e.get("word_count","")} words</small></li>')
    if cur is not None:
        items.append("</ul>")
    listing_inner = ('<article class="episode"><h1>Episodes (preview)</h1>'
                     + "\n".join(items) + "</article>")
    listing = render_liquid(def_layout, {"title": "Episodes"}, listing_inner)
    for path in ("index.html", "episodes/index.html"):
        dest = os.path.join(OUT, path)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(listing)

    print(f"Rendered {len(episodes)} episode(s) to {OUT}/")
    print("Next:  cd _preview && python3 -m http.server 4000")
    print("Open:  http://localhost:4000/")


if __name__ == "__main__":
    main()
