from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

api_key = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

class Request(BaseModel):
    candidateId: str
    jobId: str

@app.post("/webhook")
def webhook(req: Request):
    try:
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
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return {
            "result": response.choices[0].message.content
        }

    except Exception as e:
        return {
            "error": str(e)
        }

@app.get("/")
def root():
    return {
        "message": "Agent IA running"
    }
