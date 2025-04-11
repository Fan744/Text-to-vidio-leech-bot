# SudoR2spr BILLA
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os

API_ID    = os.environ.get("API_ID", "28962746")
API_HASH  = os.environ.get("API_HASH", "727457f88d661b08e636188a949cd9f3")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

BILLA = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

