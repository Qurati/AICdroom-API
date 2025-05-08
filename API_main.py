from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import ast
from giga import get_giga_answer
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

class RequestBody(BaseModel):
    ai: str
    messages: List[Message]

@app.post("/request")
async def handle_request(data: RequestBody):
    try:
        ai = data.ai
        messages = [m.dict() for m in data.messages]
        if ai == 'Yandex':
            return {"answer": get_yandex_answer(messages)}
    except Exception as e:
        return {'answer': 'Internal Error'}

@app.get("/requestGiga={msg}")
async def handle_requestGiga(msg):
    try:
        return {"answer": get_giga_answer(msg)}
    except Exception as e:
        return {'answer': 'Internal Error'}