#!/bin/sh
# Rebuild the whole blog: render posts with pandoc, then regenerate
# blog/index.html, blog/tag/*/index.html and blog/feed.xml.
# Pass .md paths to render only those posts (the index is always rebuilt).
set -e
cd "$(dirname "$0")/.."
python3 scripts/build_posts.py "$@"
python3 scripts/build_index.py
