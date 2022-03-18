import os
from dotenv import load_dotenv

load_dotenv()

#BOT INFO
TOKEN = os.getenv("TOKEN") or "No token found. Check the .env file."
CLIENT_ID = os.getenv("CLIENT_ID") or "No client ID found. Check the .env file."
GUILD_ID = os.getenv("GUILD_ID") or "No guild ID found. Check the .env file."

#DATABASE CONNECTION
DB_PROTOCOL= os.getenv("DB_PROTOCOL") or "Invalid Protocol."
DB_USER = os.getenv("DB_USER") or "Invalid User."
DB_PSSWD = os.getenv("DB_PSSWD") or "Invalid Pasword."
DB_HOST = os.getenv("DB_HOST") or "Invalid Host."
DB_PORT = os.getenv("DB_PORT") or "Invalid Port."
DB_DATABASE = os.getenv("DB_DATABASE") or "Invalid Database"
ENGINE_URL = os.getenv("ENGINE_URL") or "Invalid URL"
