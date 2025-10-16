#!/usr/bin/env bash
set -e
if [ -z "$1" ]; then
  echo "Usage: ./push_to_github.sh <your-github-username> [repo-name]"
  exit 1
fi
USER="$1"
REPO="${2:-chempop-virtual-lab}"
git init
git branch -M main || true
git add .
git commit -m "CHEMPOP Virtual Lab — initial release"
git remote remove origin 2>/dev/null || true
git remote add origin "https://github.com/${USER}/${REPO}.git"
git push -u origin main
echo "Pushed to https://github.com/${USER}/${REPO}"
