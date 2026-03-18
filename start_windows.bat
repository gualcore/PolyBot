@echo off
setlocal enabledelayedexpansion

echo ======================================================
echo           POLYBOT: AUTOMATED STARTUP (WINDOWS)
echo ======================================================

:: Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python is not installed or not in PATH.
    echo [*] Attempting to install Python via winget...
    winget install Python.Python.3.12 --silent --accept-package-agreements --accept-source-agreements
    if !errorlevel! neq 0 (
        echo [!] Auto-install failed. Please install Python manually: https://www.python.org/downloads/
        pause
        exit /b
    )
    echo [x] Python installed successfully. Please restart this script.
    pause
    exit /b
)

:: Check for Node.js
node -v >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Node.js is not installed.
    echo [*] Attempting to install Node.js via winget...
    winget install OpenJS.NodeJS --silent --accept-package-agreements --accept-source-agreements
    if !errorlevel! neq 0 (
        echo [!] Auto-install failed. Please install Node.js manually: https://nodejs.org/
        pause
        exit /b
    )
    echo [x] Node.js installed successfully. Please restart this script.
    pause
    exit /b
)

echo [x] Environment check passed.
echo [*] Installing requirements...
python -m pip install -r requirements.txt --quiet

echo [*] Launching PolyBot...
start http://localhost:5000
python main.py

pause
