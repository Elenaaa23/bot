@echo off

call %~dp0python_bot\venv\Scripts\activate

cd %~dp0python_bot


set TOKEN=5030267119:AAF3N_rYkRIx18gIQ90hMdIBxd0jxLLExoA
REM set APP_URL="https://botcar223.herokuapp.com/" + TOKEN

python bot.py

pause