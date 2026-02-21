@echo off
title Talli SMS Gateway Server
echo Starting Talli Digital Database...
echo.

:: Navigate to the directory
cd /d "%~dp0"

:: Start the Python server using uv in a new window
echo [1/2] Starting Python Backend...
start "Talli Backend" /min uv run app.py

:: Wait for server to initialize
echo Waiting for server to start...
timeout /t 5 /nobreak > nul

:: Open the web page in the default browser
echo [2/2] Opening Talli Web Page...
start http://localhost:5000

echo.
echo ==========================================
echo Talli is now RUNNING! 🚀
echo.
echo Please keep this window open while using.
echo To stop, close this window and the backend.
echo ==========================================
pause
