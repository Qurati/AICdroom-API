import requests
from config import *

def get_yandex_answer(messages):
    try:
        headers = {
            "Authorization": f"Api-Key {YandexGPT_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "modelUri": "gpt://b1gmmp5rqqqih8ridk52/yandexgpt-lite",
            "completionOptions": {"stream": False, "temperature": 0.7, "maxTokens": 2000},
            "messages": messages
        }
        res = requests.post("https://llm.api.cloud.yandex.net/foundationModels/v1/completion", headers=headers,
                            json=payload)
        data = res.json()
        return {"answer": data["result"]["alternatives"][0]["message"]["text"], "status": True}
    except Exception as e:
        return {"answer": f"Ошибка YandexGPT: {e}", "status": False}