from fastapi import FastAPI, Request
import requests
from openai import OpenAI

app = FastAPI()

# IMPORTANT: on met une clé temporaire pour éviter erreur
client = OpenAI(api_key="sk-REPLACE_ME")

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    print("✅ Nouveau candidat reçu :", data)

    return {"status": "processed"}
