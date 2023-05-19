import pandas as pd


def load_nba_data() -> pd.DataFrame:
    """Load nba data for the 22/23 season as a Pandas Dataframe

    Returns:
        pd.DataFrame: stats for the 22/23 season
    """
    return pd.read_csv("season_stats.csv")


def create_player_bio_dict(player: pd.DataFrame) -> dict:
    """Create the bio of a player

    Args:
        player (pd.DataFrame): the season's stats of a player

    Returns:
        dict: their formatted bio
    """
    return {
        'name':player['player'],
        'player_id':player['rank'],        
        'position':player['position'],
        'age':player['age'],
        'team':player['team']
        }


def create_player_defense_dict(player: pd.DataFrame) -> dict:
    """Formats a player's defensive stats

    Args:
        player (pd.DataFrame): the season's stats of a player

    Returns:
        dict: their formatted defensive stats
    """
    return {
        f"{player['player']}":{
        'appearances': {
        'games_played':player['games'],
        'mins_played':player['mins_played']
        },
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


def create_player_offense_dict(player: pd.DataFrame) -> dict:
    """Formats a player's offensive stats

    Args:
        player (pd.DataFrame): the season's stats of a player

    Returns:
        dict: their formatted offensive stats
    """
    return {
        f"{player['player']}":{
        'appearances': {
        'games_played':player['games'],
        'mins_played':player['mins_played']
        },
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


def create_player_dict(player:pd.DataFrame) -> dict:
    """Collects all the formatted data on a player together
    to produce their complete profile

    Args:
        player (pd.DataFrame): the season's stats of a player

    Returns:
        dict: their formatted complete overview for the season
    """
    return {
        player['player']: {
        'bio': create_player_bio_dict(player), 
        'offense': create_player_offense_dict(player),
        'defense': create_player_defense_dict(player),
        }
    }


def player_profile() -> list:
    """Collects all the profiles for every player in the NBA 
    for the 22/23 season and organises them in a list

    Returns:
        list: the complete list of player profiles for the season
    """
    players = load_nba_data()
    players_bio = [create_player_dict(player) for i,player in players.iterrows()]
    return players_bio


player_profiles = player_profile()


def player_name(player: dict) -> str:
    """Extracts the player name from the formatted overview
    of the player's season

    Args:
        player (dict): formatted season overview of a player

    Returns:
        str: the player's name
    """
    return list(player.keys())[0]


def name_matches(first_name: str, surname: str, player: dict) -> bool:
    """Checks whether the name given in a request matches the 
    name of the player in the API

    Args:
        first_name (str): first name provided in the request
        surname (str): surname provided in the request
        player (dict): name of the player currently being checked
    Returns: 
        bool: whether it is true or not that the names match
    """
    return player_name(player).lower() == first_name.lower() + ' ' + surname.lower()
    

def player_profiles_by_name(first_name: str, surname: str) -> dict:
    """Finds the season overview of the player who's name
    matches

    Args:
        first_name (str): the requested player's first name
        surname (str): the requested player's surname
    Returns:
        dict: the season overview of the requested player
    """
    players = player_profiles

    for player in players:
        if name_matches(first_name, surname, player):
            return player


def delete_players(first_name: str, surname: str) -> dict:
    """Removes the season overview of the player who's name
    matches

    Args:
        first_name (str): the requested player's first name
        surname (str): the requested player's surname

    Returns:
        list: the season overview of every other player in the NBA
    """
    players = player_profiles

    for player in players.copy():
        if name_matches(first_name, surname, player):
            players.remove(player)

    return f"{first_name} {surname}'s stats for the 22/23 season have been deleted!"


def player_bios(player_profiles: list) -> list:
    """Collects the bios for every player in the NBA

    Args: 
        player_profiles (list): the season overview of every player
    Returns:
        list: the bio of every player
    """
    return [player.get(player_name(player)).get('bio') for player in player_profiles]


all_bios = player_bios(player_profiles)


def player_bio_by_name(first_name: str, surname: str) -> dict:
    """Finds the bio of the player who's name
    matches

    Args:
        first_name (str): the requested player's first name
        surname (str): the requested player's surname
    Returns:
        dict: the bio of the requested player
    """
    players = player_profiles

    for player in players:
        if name_matches(first_name, surname, player):
            return player.get(player_name(player)).get('bio')

def player_offense_stats(player_profiles: list) -> list:
    """Collects just the offensive stats of every active NBA
    player for the season

    Args: 
        player_profiles (list): the season overview of every player

    Returns:
        list: the offensive stats of every player
    """
    return [{player_name(player):player.get(player_name(player)).get('offense')} for player in player_profiles]


players_offense = player_offense_stats(player_profiles)


def player_defense_stats(player_profiles: list) -> list:
    """Creates a list of dictionaries containing player defensive stats

    Args: 
        player_profiles (list): the season overview of every player
    Returns:
        list: the defensive stats of every player
    """
    return [{player_name(player):player.get(player_name(player)).get('defense')} for player in player_profiles]


players_defense = player_defense_stats(player_profiles)


def player_offense_by_name(first_name: str, surname: str) -> dict:
    """Finds the season offensive stats of the player who's name
    matches

    Args:
        first_name (str): the requested player's first name
        surname (str): the requested player's surname
    Returns:
        dict: the offensive stats of the requested player
    """
    players = player_profiles

    for player in players:
        if name_matches(first_name, surname, player):
            return player.get(player_name(player)).get('offense')


def player_defense_by_name(first_name: str, surname: str) -> dict:
    """Finds the season defensive stats of the player who's name
    matches

    Args:
        first_name (str): the requested player's first name
        surname (str): the requested player's surname
    Returns:
        dict: the defensive stats of the requested player
    """
    players = player_profiles

    for player in players:
        if name_matches(first_name, surname, player):
            return player.get(player_name(player)).get('defense')




    
