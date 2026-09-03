"""
SUFIA AI Trading Bot - One Click Launcher
Starts the Web Server, API Engine, and opens the Trading Bot UI in Browser
"""

import os
import sys
import time
import webbrowser
import threading
import uvicorn

def open_browser():
    time.sleep(1.5)
    url = "http://localhost:8000"
    print(f"\n🌐 Opening SUFIA AI Trading Bot in your browser: {url}")
    webbrowser.open(url)

def main():
    print("=" * 65)
    print("  👑 SUFIA AI TRADING BOT — TARIK")
    print("  🔥 All Buttons, Voice AI, Signals & Auto Trade are READY!")
    print("=" * 65)
    print("\n[+] Starting FastAPI Web Server & AI Engine on http://localhost:8000 ...")
    
    # Open browser in a separate thread
    threading.Thread(target=open_browser, daemon=True).start()

    from server import app
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

if __name__ == "__main__":
    main()
