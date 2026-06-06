import os
from fastapi import FastAPI
from pydantic import BaseModel
import requests

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://host.docker.internal:11434/api/generate"
)
app = FastAPI(title="AI Inference Platform")

OLLAMA_URL =  OLLAMA_URL

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"message": "AI Inference Platform Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/ask")
def ask(request: PromptRequest):
    payload = {
        "model": "tinyllama",
        "prompt": request.prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()
