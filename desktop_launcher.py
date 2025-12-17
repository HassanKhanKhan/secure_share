import webview
import threading
import os
import sys

def start_django():
    os.system(f"{sys.executable} manage.py runserver")

# Run Django in background
threading.Thread(target=start_django, daemon=True).start()

# Open window pointing to login page
webview.create_window("Secure File Manager", "http://127.0.0.1:8000/login/")
webview.start()
