import openai
import ast
from config import proxies, openAI_key

openai.proxy = ast.literal_eval(proxies)
openai.api_key = openAI_key
def get_gpt_answer(messages, model):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
        )
        answer = response.choices[0].message['content']
        return {"answer": answer, "status": True}
    except Exception as e:
        return {"answer": f"Ошибка GPT: {e}", "status": False}


def get_gpt_answer_inline(text, user_id, model, role_text):
    try:
        messages = [{"role": "system", "content": role_text}, {"role": "user", "content": text}]
        response = openai.ChatCompletion.create(model=model, messages=messages)
        return {"answer": response.choices[0].message['content'], "status": True}
    except Exception as e:
        return {"answer": f"Ошибка GPT: {e}", "status": False}