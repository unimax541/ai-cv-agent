from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

# Créer l'application FastAPI
app = FastAPI()

# Initialiser le client OpenAI avec la clé
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Définir le format de la requête
class Request(BaseModel):
    candidateId: str
    jobId: str

# Endpoint webhook
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

# Route simple pour tester que l'app fonctionne
@app.get("/")
def root():
