#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}")" && pwd)"
cd $DIR
source venv/bin/activate
git config --global --add safe.directory $DIR
git add .
git commit -m "update by bot"
git pull
git push
python3 main.py
# python3 test.py
git add .
git commit -m "update by bot"
git push
