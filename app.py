from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

# Création de l'app FastAPI
app = FastAPI()

# Initialisation OpenAI (utilise la clé dans Render)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Format des données reçues
class Request(BaseModel):
    candidateId: str
    jobId: str

# Endpoint principal IA
@app.post("/webhook")
def webhook(req: Request):
    prompt = f"""
Tu es un expert en recrutement.

Analyse ce candidat : {req.candidateId}
pour ce poste : {req.jobId}

Donne :
- Score sur 100
- 3 forces
- 3 faiblesses
- Verdict final
"""

    response = client.chat.completions.create(
        model="gpt-5-chat",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "result": response.choices[0].message.content
    }

# Route simple (important pour éviter les erreurs)
@app.get("/")
def root():
    return {"message": "Agent IA running 🚀"}
