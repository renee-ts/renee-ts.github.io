#!/usr/bin/env python3

import datetime
import html
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOG = ROOT / "blog"
POSTS = BLOG / "posts"
SITE_URL = "https://renee-ts.github.io"
FEED_TITLE = "Renee's Blog"
FEED_DESC = "Math, AI safety research, and game development."


def _scalar(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    if v in ("true", "false"):
        return v == "true"
    return v


def parse_front_matter(text):
    """Minimal parser for the flat `key: value` / `key: [a, b]` front matter
    used by the posts. Returns {} if the file has no front matter."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    meta = {}
    for line in lines[1:]:
        if line.strip() in ("---", "..."):
            return meta
        m = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            meta[key] = [_scalar(x) for x in val[1:-1].split(",") if x.strip()]
        else:
            meta[key] = _scalar(val)
    return {}


def load_posts():
    posts = []
    for md in sorted(POSTS.rglob("*.md")):
        meta = parse_front_matter(md.read_text(encoding="utf-8"))
        if not meta.get("title") or not meta.get("date"):
            continue
        if meta.get("draft") is True:
            continue
        tags = meta.get("tags") or []
        if isinstance(tags, str):
            tags = [tags]
        posts.append({
            "title": meta["title"],
            "description": meta.get("description", ""),
            "date": str(meta["date"]),
            "tags": tags,
            "url": "/" + md.with_suffix(".html").relative_to(ROOT).as_posix(),
        })
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


PAGE_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Blog</title>
  <link rel="stylesheet" href="/style.css" />
  <link rel="alternate" type="application/rss+xml" title="Renee's Blog" href="/blog/feed.xml" />
  <style>
    .blog-container {
      display: flex;
      gap: 2rem;
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem;
    }

    .blog-main {
      flex: 1;
      min-width: 600px;
    }

    .blog-sidebar {
      width: 200px;
      flex-shrink: 0;
    }

    .tag-button {
      display: block;
      padding: 0.5rem 1rem;
      margin-bottom: 0.5rem;
      background: var(--color-gray-5);
      color: var(--color-maroon);
      text-decoration: none;
      border-radius: 4px;
      font-size: 0.9rem;
      transition: background 0.2s;
    }

    .tag-button:hover {
      background: var(--color-gray-4);
    }

    .tag-count {
      font-size: 0.85em;
      color: var(--color-gray-3);
      margin-left: 0.3rem;
    }

    .post-item {
      margin-bottom: 2rem;
      padding-bottom: 2rem;
      border-bottom: 1px solid var(--color-gray-5);
    }

    .post-item h3 {
      margin: 0 0 0.5rem 0;
      font-size: 1.3rem;
    }

    .post-item h3 a {
      color: var(--color-maroon);
      text-decoration: none;
    }

    .post-item h3 a:hover {
      color: var(--color-gray-2);
    }

    .post-item-desc {
      color: var(--color-gray-1);
      font-size: 0.95rem;
      margin: 0.25rem 0;
    }

    .post-item-meta {
      color: var(--color-gray-2);
      font-size: 0.9rem;
      margin: 0.25rem 0;
    }

    .post-item-tags {
      color: var(--color-gray-2);
      font-size: 0.85rem;
      margin: 0.5rem 0 0 0;
    }

    .post-item-tags a {
      color: var(--color-maroon);
      text-decoration: none;
      margin-right: 1rem;
    }

    .post-item-tags a:hover {
      color: var(--color-gray-1);
    }

    .back-link {
      display: inline-block;
      margin-bottom: 1.5rem;
      color: var(--color-gray-2);
      text-decoration: none;
      font-size: 0.9rem;
    }

    .back-link:hover {
      color: var(--color-maroon);
    }

    .feed-link {
      display: inline-block;
      margin-top: 1rem;
      color: var(--color-gray-2);
      text-decoration: none;
      font-size: 0.8rem;
      letter-spacing: 0.05em;
    }

    .feed-link:hover {
      color: var(--color-maroon);
    }

    .sidebar-header {
      font-weight: bold;
      color: var(--color-maroon);
      margin-bottom: 1rem;
      font-size: 0.95rem;
      text-transform: uppercase;
      font-size: 0.8rem;
      letter-spacing: 0.05em;
    }

    @media (max-width: 900px) {
      .blog-container {
        flex-direction: column;
      }
      .blog-sidebar {
        width: 100%;
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
      }
      .tag-button {
        display: inline-block;
        margin-bottom: 0;
      }
    }
  </style>
</head>
<body>
<div class="blog-container">
  <main class="blog-main">
    <a class="back-link" href="/">← back</a>
    <h1>Blog</h1>
"""


def tag_url(tag):
    return f"/blog/tag/{tag}/index.html"


def render_post_item(p):
    e = html.escape
    tags = " ".join(f'<a href="{tag_url(t)}">{e(t)}</a>' for t in p["tags"])
    out = [
        '    <article class="post-item">',
        f'      <h3><a href="{p["url"]}">{e(p["title"])}</a></h3>',
    ]
    if p["description"]:
        out.append(f'      <p class="post-item-desc">{e(p["description"])}</p>')
    out.append(f'      <p class="post-item-meta">{e(p["date"])}</p>')
    if p["tags"]:
        out.append(f'      <p class="post-item-tags">{tags}</p>')
    out.append("    </article>")
    return "\n".join(out) + "\n"


def render_page(posts, tag_counts):
    parts = [PAGE_HEAD]
    parts.extend(render_post_item(p) for p in posts)
    parts.append("  </main>\n\n")
    parts.append('  <aside class="blog-sidebar">\n')
    parts.append('    <div class="sidebar-header">Tags</div>\n')
    for tag, n in tag_counts:
        parts.append(
            f'        <a href="{tag_url(tag)}" class="tag-button">'
            f'{html.escape(tag)} <span class="tag-count">({n})</span></a>\n'
        )
    parts.append('    <a href="/blog/feed.xml" class="feed-link">RSS</a>\n')
    parts.append("  </aside>\n</div>\n</body>\n</html>")
    return "".join(parts)


_DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
_MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def rfc822(date_str):
    d = datetime.date.fromisoformat(date_str)
    return (f"{_DAYS[d.weekday()]}, {d.day:02d} {_MONTHS[d.month - 1]} "
            f"{d.year} 00:00:00 +0000")


def render_feed(posts):
    e = lambda s: html.escape(s, quote=False)
    out = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
        "  <channel>",
        f"    <title>{e(FEED_TITLE)}</title>",
        f"    <link>{SITE_URL}/blog/index.html</link>",
        f"    <description>{e(FEED_DESC)}</description>",
        f'    <atom:link href="{SITE_URL}/blog/feed.xml" rel="self" '
        'type="application/rss+xml" />',
    ]
    for p in posts:
        link = SITE_URL + p["url"]
        out += [
            "    <item>",
            f"      <title>{e(p['title'])}</title>",
            f"      <link>{link}</link>",
            f'      <guid isPermaLink="true">{link}</guid>',
            f"      <pubDate>{rfc822(p['date'])}</pubDate>",
        ]
        if p["description"]:
            out.append(f"      <description>{e(p['description'])}</description>")
        out += [f"      <category>{e(t)}</category>" for t in p["tags"]]
        out.append("    </item>")
    out += ["  </channel>", "</rss>"]
    return "\n".join(out) + "\n"


def main():
    posts = load_posts()

    counts = {}
    for p in posts:
        for t in p["tags"]:
            counts[t] = counts.get(t, 0) + 1
    tag_counts = sorted(counts.items())

    (BLOG / "index.html").write_text(render_page(posts, tag_counts), encoding="utf-8")

    tag_dir = BLOG / "tag"
    if tag_dir.exists():
        shutil.rmtree(tag_dir)
    for tag, _ in tag_counts:
        d = tag_dir / tag
        d.mkdir(parents=True)
        tagged = [p for p in posts if tag in p["tags"]]
        (d / "index.html").write_text(render_page(tagged, tag_counts), encoding="utf-8")

    (BLOG / "feed.xml").write_text(render_feed(posts), encoding="utf-8")

    print(f"{len(posts)} posts, {len(tag_counts)} tags -> "
          "blog/index.html, blog/tag/*/index.html, blog/feed.xml")


if __name__ == "__main__":
    main()
