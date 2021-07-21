import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
admins = [os.getenv("ADMINS")]
ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

channels = []

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}