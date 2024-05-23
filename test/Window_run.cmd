@echo off
REM Get the directory of the script
set DIR=%~dp0
cd /d %DIR%
if not exist Telegram-message-forwarder (
    call git clone https://github.com/piriyaraj/Telegram-message-forwarder.git
)
cd Telegram-message-forwarder
if not exist venv (
    python -m venv venv
)

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
@REM git restore .
@REM git pull

REM Run the Python script
python main.py
REM python test.py
