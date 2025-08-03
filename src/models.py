from typing import List, Tuple
from pydantic import BaseModel, EmailStr

class PlayersRequest(BaseModel):
    players: List[str]

class MatchResponse(BaseModel):
    title: str
    players: Tuple[str, str]
    
class ScheduleResponse(BaseModel):
    matches: List[MatchResponse]
    
class TieResponse(BaseModel):
    points: List[int]
    satisfies_landau: bool
    players_tied: int 
    
class TiesResponse(BaseModel):
    total_players: int
    ties: List[TieResponse]