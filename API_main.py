from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from giga import get_giga_answer
from gpt import get_gpt_answer
from yandex import *
from pydantic import BaseModel
from typing import List, Literal
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    text: str

class MessageGPT(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str

class RequestBody(BaseModel):
    ai: str
    messages: List[Message]

class RequestBodyGPT(BaseModel):
    ai: str
    messages: List[MessageGPT]
    model: str

@app.get("/")
def home_page():
    return {"answer": "API home page"}

@app.post("/request")
async def handle_request(data: RequestBody):
    try:
        ai = data.ai
        messages = [m.dict() for m in data.messages]
        print(data)
        if ai == 'Yandex':
            return {"answer": get_yandex_answer(messages)}
    except Exception as e:
        return {'answer': 'Internal Error'}

@app.post("/requestGPT")
async def handle_requestGPT(data: RequestBodyGPT):
    try:
        model = data.model
        messages = [m.dict() for m in data.messages]
        return {"answer": get_gpt_answer(messages, model)}
    except Exception as e:
        return {'answer': 'Internal Error'}

@app.get("/requestGiga={msg}")
async def handle_requestGiga(msg):
    try:
        return {"answer": get_giga_answer(msg)}
    except Exception as e:
        return {'answer': 'Internal Error'}

