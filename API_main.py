from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from API.yandex import *
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/request={req}&ai={ai}&role={role}&user_id={user_id}")
def get_token(req: str, ai: str):
    try:
        if ai == 'Yandex':
            sd
            return {"answer": get_yandex_answer_inline(req, 'assistant')}
    except Exception as e:
        return {'answer': f'Error: {e}'}