import json

from pydantic import BaseModel
from fastapi import FastAPI, status, Query
from typing import Optional

from .api_utils import (all_bios, delete_players, player_bio_by_name,
                        player_defense_by_name, player_name,
                        player_offense_by_name, player_profiles,
                        player_profiles_by_name, players_defense,
                        players_offense)

class Player(BaseModel):
    name: str 
    player_id: Optional[int] = None 
    position: str
    age: int
    team: str


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

@app.get('/players/bio')
async def players_bio():
    return all_bios

@app.get('/players/bio/')
async def players_bio_by_name(first_name: str, surname: str):
    return player_bio_by_name(first_name, surname)

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

@app.post('/players/bio/')
async def post_new_player(player: Player):
    id = max([player.get('player_id') for player in all_bios]) + 1
    new_player = {
        'name': player.name,
        'player_id':id,
        'position':player.position,
        'age':player.age,
        'team':player.team
    }
    all_bios.append(new_player)
    return new_player

@app.put('/players/bio/')
async def update_player(player: Player):
    new_player = {
        'name': player.name,
        'player_id':player.player_id,
        'position':player.position,
        'age':player.age,
        'team':player.team
    }
    player_to_remove = [bio for bio in all_bios if bio.get('player_id') == player.player_id]
    all_bios.remove(player_to_remove[0])
    all_bios.append(new_player)
    return new_player