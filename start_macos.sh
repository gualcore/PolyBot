#!/bin/bash

echo "======================================================"
echo "          POLYBOT: AUTOMATED STARTUP (MACOS)"
echo "======================================================"

# Check for Python 3
if ! command -v python3 &> /dev/null
then
    echo "[!] Python3 is not installed."
    echo "[*] Please install it via Homebrew: brew install python"
    echo "    Or download from: https://www.python.org/downloads/"
    exit
fi

# Check for Node.js
if ! command -v node &> /dev/null
then
    echo "[!] Node.js is not installed."
    echo "[*] Please install it via Homebrew: brew install node"
    echo "    Or download from: https://nodejs.org/"
    exit
fi

echo "[x] Environment check passed."
echo "[*] Installing requirements..."
python3 -m pip install -r requirements.txt --quiet

echo "[*] Launching PolyBot..."
open "http://localhost:5000"
python3 main.py
