#!/usr/bin/env python3

import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_index import POSTS, ROOT, parse_front_matter

TEMPLATE = ROOT / "template.html"


def readtime_filter(md):
    if md.relative_to(POSTS).parts[0] == "dev":
        return ROOT / "readtime.lua"
    return ROOT / "math_readtime.lua"


def render(md):
    text = md.read_text(encoding="utf-8")
    meta = parse_front_matter(text)
    if not meta or meta.get("draft") is True:
        out = md.with_suffix(".html")
        if out.exists():
            out.unlink()
        print(f"skip (draft): {md.relative_to(ROOT)}")
        return
    cmd = [
        "pandoc", md.name,
        "--standalone",
        f"--template={TEMPLATE}",
        "--math-method=mathjax",
        f"--lua-filter={readtime_filter(md)}",
        f"--lua-filter={ROOT / 'footnotes.lua'}",
    ]
    if meta.get("toc") is True:
        cmd.append("--toc")
    if "tikzcd" in text:
        cmd.append(f"--lua-filter={ROOT / 'tikzcd.lua'}")
    cmd += ["-o", md.with_suffix(".html").name]
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
