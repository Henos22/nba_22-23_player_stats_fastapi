from fastapi import FastAPI

from api_utils import (delete_players, player_profiles,#change_players_team,
                       player_profiles_by_name, players_defense,
                       players_offense)

app = FastAPI()

@app.get('/')
async def root():
    return "Welcome to the NBA 22-23 Season Player Breakdown"

@app.get('/players')
async def players():
    return player_profiles

@app.get('/players/')
async def player_by_name(first_name: str, surname: str):
    return player_profiles_by_name(first_name,surname)

@app.delete('/players/')
async def remove_player_by_name(first_name: str, surname: str):
    return delete_players(first_name,surname)

# @app.patch('/players/')
# async def adjust_players_team(team: str):
#     return change_players_team(team)