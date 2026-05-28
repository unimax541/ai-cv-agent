from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ✅ définir le format attendu
class WebhookData(BaseModel):
    candidateId: str
    jobId: str

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/webhook")
async def webhook(data: WebhookData):
    print("✅ Candidat reçu :", data)

    return {"status": "processed"}
