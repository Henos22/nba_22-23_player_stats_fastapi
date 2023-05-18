import pandas as pd


def load_nba_data() -> pd.DataFrame:
    """Load nba data for the 22/23 season as a Pandas Dataframe

    Returns:
        pd.DataFrame: stats for the 22/23 season
    """
    return pd.read_csv("season_stats.csv")

def create_player_bio_dict(player:pd.DataFrame) -> dict:
    """Formats data that would be present in a player's bio

    Args:
        player (pd.DataFrame): a single player's details

    Returns:
        dict: formatted bio data
    """
    return {
        'player_id':player['rank'],
        'first_name':player['player'].split(' ')[0],
        'surname':player['player'].split(' ')[1],
        'position':player['position'],
        'age':player['age'],
        'team':player['team']
    }

def player_profile() -> list:
    """Creates a list of dictionaries containing player bio data

    Returns:
        list: list of player data
    """
    df = load_nba_data()
    player_df = df.filter(regex = "rank|player|position|age|team")
    players_bio = [create_player_bio_dict(player) for i,player in player_df.iterrows()]
    return players_bio

player_profiles = player_profile()

def player_profiles_by_name(first_name: str, surname: str) -> dict:
    """Gets the bios of players who have been requested by id

    Args:
        ids (list): list of player ids

    Returns:
        list: list of the selected players' bios 
    """
    all_bios = player_profiles
    for bio in all_bios:
        if bio['first_name'].lower() == first_name.lower() and bio['surname'].lower() == surname.lower():
            return bio

def create_player_offense_dict(player: pd.DataFrame) -> dict:
    """Formats a player's offensive stats

    Args:
        player (pd.DataFrame): all recorded stats for a player

    Returns:
        dict: formatted stats
    """
    return {
        f"{player['player']}":{
        'games_played':player['games'],
        'mins_played':player['mins_played'],
        'total_points':player['points'],
        'points_per_game':round(player['points']/player['games'],2),
        'field_goals':{
            'field_goal_attempts':player['FGA'],
            'field_goals':player['FG'],
            'field_goal_percentage':player['FG%']
        },
        '3_pointers':{
            '3_point_attempts':player['3PA'],
            '3_point_shots_made':player['3P'],
            '3_point_percentage':player['3P%']
        },
        '2_pointers':{
            '2_point_attempts':player['2PA'],
            '2_point_shots_made':player['2P'],
            '2_point_percentage':player['2P%']
        },
        'effective_field_goal_percentage':player['eFG%'],
        'free_throws':{
            'free_throw_attempts':player['FTA'],
            'free_throws_made':player['FT'],
            'free_throws_percentage':player['FT%']
        },
        'assists':{
            'total_assists':player['AST'],
            'assists_per_game':round(player['AST']/player['games'],2)
        }
    }
}

def player_offense_stats() -> list:
    """Creates a list of dictionaries containing player shooting/scoring stats

    Returns:
        list: list of player stats
    """
    df = load_nba_data()
    player_df = df.filter(regex = "player|games|mins_played|FG|FGA|FG%|3P|3PA|3P%|2P|2PA|2P%|eFG%|FT|FTA|FT%|points|AST")
    players_offense = [create_player_offense_dict(player) for i,player in player_df.iterrows()]
    return players_offense

players_offense = player_offense_stats()

def create_player_defense_dict(player: pd.DataFrame) -> dict:
    """Formats a player's defensive stats

    Args:
        player (pd.DataFrame): all recorded stats for a player

    Returns:
        dict: formatted stats
    """
    return {
        f"{player['player']}":{
            'games_played':player['games'],
            'mins_played':player['mins_played'],
            'rebounding':{
                'total_rebounds':player['TRB'],
                'offensive_rebounds':player['ORB'],
                'offensive_rebounds':round(player['ORB']/player['games'],2),
                'defensive_rebounds':player['DRB'],
                'defensive_rebounds_per_game':round(player['DRB']/player['games'],2)
            },
            'steals':{
                'steals':player['STL'],
                'steals_per_game':round(player['STL']/player['games'],2)
            },
            'blocks':{
                'blocks':player['BLK'],
                'blocks_per_game':round(player['BLK']/player['games'],2)
            },
            'turnovers':{
                'turnovers':player['TOV'],
                'turnovers_per_game':round(player['TOV']/player['games'],2)
            },
            'fouls':{
                'fouls':player['fouls'],
                'fouls_per_game':round(player['fouls']/player['games'],2)
        }
    }
}

def player_defense_stats() -> list:
    """Creates a list of dictionaries containing player defensive stats

    Returns:
        list: list of player stats
    """
    df = load_nba_data()
    player_df = df.filter(regex = "player|games|mins_played|ORB|DRB|TRB|STL|BLK|TOV|fouls")
    players_defense = [create_player_defense_dict(player) for i,player in player_df.iterrows()]
    return players_defense  

players_defense = player_defense_stats()

def delete_players(first_name: str, surname: str) -> dict:
    """Removes the bios of the players that have been selected in the DELETE request

    Args:
        id (list): ids of the players to be removed

    Returns:
        list: players remaining
    """
    players = player_profiles
    
    for player in players.copy():
        if player.get('first_name') == first_name and player.get('surname') == surname:
            players.remove(player)
    return f"{first_name} {surname}'s bio has been deleted"

# def change_players_team(team: str):
    
