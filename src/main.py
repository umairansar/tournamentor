from typing import Union
from matchmaker import generate_league_round_robin_schedule
from models import PlayersRequest
from fastapi import FastAPI
import logging

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/round_robin")
def read_item(request: PlayersRequest):
    res = generate_league_round_robin_schedule(request.players)
    logging.info(res)
    return res
