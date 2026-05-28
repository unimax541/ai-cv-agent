from fastapi import FastAPI, Request
import requests
from openai import OpenAI

app = FastAPI()
client = OpenAI(api_key="TON_API_OPENAI")

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    # Simulation simple pour l’instant
    print("New candidate received:", data)

    return {"status": "processed"}
``
