# SudoR2spr BILLA
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os

API_ID    = os.environ.get("API_ID", "26537149")
API_HASH  = os.environ.get("API_HASH", "2697a63a384fd9b95520ee63530f6a75")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

BILLA = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

