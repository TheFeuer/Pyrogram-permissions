import pytz
import os

from dotenv import load_dotenv
load_dotenv()

tz = pytz.timezone('Europe/Moscow')

api_id = os.environ.get("api_id")
api_hash = os.environ.get("api_hash")
chat_id = os.environ.get("chat_id")
