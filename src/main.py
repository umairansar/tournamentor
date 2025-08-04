from fastapi import FastAPI
import logging

app = FastAPI()

@app.get("/health")
def health():
    return "Healthy"

