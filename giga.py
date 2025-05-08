from  config import *
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat
import ast


def giga_auth():
    giga = GigaChat(
        credentials=GigaChat_key,
        verify_ssl_certs=False,
    )
    return giga


def get_giga_answer(prompt):
    try:
        messages = [SystemMessage(
            content="Ты ассистент."
        ), HumanMessage(content=prompt)]
        res = giga_auth().invoke(messages)
        messages.append(res)
        return {"answer": res.content, "status": True}
    except Exception as e:
        return {"answer": f'Ошибка Giga Chat: {e}', "status": False}

