import os
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('7294993191:AAG1bDTcYRV7hMXBkPDp7okapOwcjTDntA8')

DB_NAME = os.getenv('DB_NAME', 'valyutagame_bot_db')
DB_USER = os.getenv('DB_USER', 'user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'genzdd23')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', 5432))
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

