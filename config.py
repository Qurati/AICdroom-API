import os
from dotenv import load_dotenv

load_dotenv()
openAI_key = os.getenv('openAI_key')
YandexGPT_key = os.getenv('YandexGPT_key')
GigaChat_key = os.getenv('GigaChat_key')
admins = os.getenv('admins')

proxies = os.getenv('proxies')

