import os
from dotenv import load_dotenv

load_dotenv()

#BOT INFO
TOKEN = os.getenv('TOKEN') or 'No token found. Check the .env file.'
CLIENT_ID = os.getenv('CLIENT_ID') or 'No client ID found. Check the .env file.'
GUILD_ID = os.getenv('GUILD_ID') or 'No guild ID found. Check the .env file.'

#DATABASE CONNECTION
DB_USER = os.getenv('DB_USER') or 'Invalid User.'
DB_PSSWD = os.getenv('DB_PSSWD') or 'Invalid Pasword.'
HOST = os.getenv('HOST') or 'Invalid Host.'
PORT = os.getenv('PORT') or 'Invalid Port.'
DATABASE = os.getenv('DATABASE') or 'Invalid Database'

#SQL QUERIES
FETCH_PLAYERS_ALL= os.getenv('FETCH_PLAYERS_ALL')