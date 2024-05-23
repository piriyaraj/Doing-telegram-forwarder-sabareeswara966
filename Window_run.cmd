@echo off
REM Get the directory of the script
set DIR=%~dp0
cd /d %DIR%

REM Check if virtual environment exists, if not, create it
if not exist venv (
    python -m venv venv
)

REM Activate the virtual environment
call venv\Scripts\activate

REM Install dependencies and suppress output
if exist requirements.txt (
    pip install -r requirements.txt > NUL 2>&1
)

REM Configure git
git config --global --add safe.directory %DIR%
git add .
git commit -m "update by bot"
git pull
git push

REM Run the Python script
python main.py
REM python test.py

git add .
git commit -m "update by bot"
git push
