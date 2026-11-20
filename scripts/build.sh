#!/bin/sh
set -e
cd "$(dirname "$0")/.."
python3 scripts/build_posts.py "$@"
python3 scripts/build_index.py
