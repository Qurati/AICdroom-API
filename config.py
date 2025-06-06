import os
from dotenv import load_dotenv

load_dotenv()
openAI_key = os.getenv('openAI_key')
YandexGPT_key = os.getenv('YandexGPT_key')
GigaChat_key = os.getenv('GigaChat_key')
admins = os.getenv('admins')

user_db = os.getenv('user_db')
password_db = os.getenv('password_db')
host_db = os.getenv('host_db')
database_db = os.getenv('database_db')

proxies = os.getenv('proxies')

