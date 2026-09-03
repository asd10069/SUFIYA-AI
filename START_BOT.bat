@echo off
title SUFIA AI Trading Bot - PC Edition
cd /d "C:\Users\ASAD_AFRIDY\Desktop\bot.py\BOT"
set PYTHONIOENCODING=utf-8

echo ============================================================
echo   SUFIA AI TRADING BOT - PC Edition
echo   Web App: http://localhost:8000
echo ============================================================

:: Kill any process using port 8000
for /f "tokens=5" %%a in ('netstat -aon ^| find ":8000" ^| find "LISTENING"') do (
    echo [+] Killing old process on port 8000 (PID: %%a)
    taskkill /PID %%a /F >nul 2>&1
)

:: Kill any leftover python.exe from previous run
taskkill /f /im python.exe >nul 2>&1

echo [+] Starting SUFIA AI Trading Bot...
timeout /t 1 /nobreak >nul

python run_bot.py
pause


