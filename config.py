import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN") or "No token found. Check the .env file."
CLIENT_ID = os.getenv("CLIENT_ID") or "No client ID found. Check the .env file."
GUILD_ID = os.getenv("GUILD_ID") or "No guild ID found. Check the .env file."
