import json

from fastapi import FastAPI

from .api_utils import (delete_players, player_defense_by_name,
                        player_offense_by_name, player_profiles,
                        player_profiles_by_name, players_defense,
                        players_offense)

app = FastAPI()

@app.get('/')
async def root():
    return "-- Welcome to the NBA 22-23 Season Player Breakdown --"

@app.get('/players')
async def players():
    return json.dumps(player_profiles, indent = "")

@app.get('/players/')
async def player_by_name(first_name: str, surname: str):
    return player_profiles_by_name(first_name,surname)

@app.get('/players/offense')
async def get_players_offense():
    return json.dumps(players_offense)

@app.get('/players/offense/')
async def get_player_offense_by_name(first_name: str, surname: str):
    return player_offense_by_name(first_name,surname)

@app.get('/players/defense')
async def get_players_defense():
    return json.dumps(players_defense)

@app.get('/players/defense/')
async def get_player_defense_by_name(first_name: str, surname: str):
    return player_defense_by_name(first_name,surname)

@app.delete('/players/')
async def remove_player_by_name(first_name: str, surname: str):
    return delete_players(first_name,surname)
