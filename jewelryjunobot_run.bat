@echo off

call %~dp0jewelryjunobot\venv\Scripts\activate

cd %~dp0jewelryjunobot

set TOKEN="token"

python jewelryjuno_bot.py

pause