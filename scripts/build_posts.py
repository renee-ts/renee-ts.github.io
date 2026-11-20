#!/usr/bin/env python3
"""Render every blog/posts/**/*.md to a sibling .html with pandoc, using
template.html and the Lua filters in the repo root.

Posts without front matter are treated as drafts and skipped.

Usage:
  python3 scripts/build_posts.py              # all posts
  python3 scripts/build_posts.py PATH.md ...  # just these posts

RECONSTRUCTED 2026-11-20 after the original scripts were lost. Verified with
pandoc 3.14: reproduces the committed HTML of every post byte-for-byte,
except multi-line $$ display math, where newer pandoc trims whitespace.
"""

import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_index import POSTS, ROOT, parse_front_matter  # noqa: E402

TEMPLATE = ROOT / "template.html"


def readtime_filter(md):
    # Inferred: gamedev posts (blog/posts/dev) match 120 wpm (readtime.lua);
    # math posts match 60 wpm (math_readtime.lua).
    if md.relative_to(POSTS).parts[0] == "dev":
        return ROOT / "readtime.lua"
    return ROOT / "math_readtime.lua"


def render(md):
    text = md.read_text(encoding="utf-8")
    meta = parse_front_matter(text)
    if not meta:
        print(f"skip (draft, no front matter): {md.relative_to(ROOT)}")
        return
    cmd = [
        "pandoc", md.name,
        "--standalone",
        f"--template={TEMPLATE}",
        "--math-method=mathjax",  # emits \\( \\) delimiters for katex-init.js auto-render
        f"--lua-filter={readtime_filter(md)}",
    ]
    if meta.get("toc") is True:
        cmd.append("--toc")
    if "tikzcd" in text:
        cmd.append(f"--lua-filter={ROOT / 'tikzcd.lua'}")
    cmd += ["-o", md.with_suffix(".html").name]
    # Run from the post's folder so relative asset / tikz-cache paths work.
    subprocess.run(cmd, cwd=md.parent, check=True)
    print(f"built {md.with_suffix('.html').relative_to(ROOT)}")


def main():
    if shutil.which("pandoc") is None:
        sys.exit("pandoc not found on PATH")
    targets = [Path(a).resolve() for a in sys.argv[1:]] or sorted(POSTS.rglob("*.md"))
    for md in targets:
        render(md)


if __name__ == "__main__":
    main()
