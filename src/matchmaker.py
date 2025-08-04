from models import ScheduleResponse, MatchResponse, TiesResponse
from typing import List
import math

def generate_league_round_robin_schedule(players: List[str]) -> ScheduleResponse:
    schedule: List[MatchResponse] = []
    index = 1
    for i in range(len(players)):
        for j in range(i+1, len(players)):
            match = MatchResponse(title=f"Match {index}", players=(players[i], players[j]))
            schedule.append(match)
            index += 1
    return schedule

def generate_possible_ties(players: List[str]) -> TiesResponse:
    players_count = len(players)
    total_wins_possible = math.comb(players_count, 2)
    # WIP
    