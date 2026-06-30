from pydantic import BaseModel
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

class Request(BaseModel):
    candidateId: str
    jobId: str

@app.post("/webhook")
def webhook(req: Request):

    prompt = f"""
    Analyse ce candidat : {req.candidateId}
    pour ce poste : {req.jobId}

    Donne :
    - Score /100
    - 3 forces
    - 3 faiblesses
    - Verdict
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
``
