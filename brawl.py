import os
import requests
from dotenv import load_dotenv
import urllib.parse
import json 
import os
from datetime import datetime
from data_manager import load_data, save_data, update_battle_archive

load_dotenv()

api_token = os.getenv('BRAWL_STARS_API_TOKEN')

headers = {
    'Authorization': f'Bearer {api_token}',
    'Accept': 'application/json'
}

def get_player_info(player_tag):
    #player_tag = player_tag.lstrip('#')
    encoded_tag = urllib.parse.quote(player_tag)
    url = f'https://api.brawlstars.com/v1/players/{encoded_tag}'
    
    #print(f"Requesting URL: {url}")  # Debug print
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        player_info = response.json()
        return player_info
    else:
        return f"Error: {response.status_code} Response: {response.text} Headers: {response.headers}"

def get_battles(player_tag):
    encoded_tag = urllib.parse.quote(player_tag)
    url = f'https://api.brawlstars.com/v1/players/{encoded_tag}/battlelog'
    
    #print(f"Requesting URL: {url}")  # Debug print
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        battle_data = response.json()
        penis = battle_data['items']
        print(f'penis: {len(penis)}')
        return battle_data
    else:
        return f"Error: {response.status_code} Response: {response.text} Headers: {response.headers}"
    
    
def get_club_info(club_tag):
    club_tag = club_tag.lstrip('#')
    encoded_tag = urllib.parse.quote(club_tag)
    url = f'https://api.brawlstars.com/v1/clubs/%23{encoded_tag}'
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
        return None

def get_player_club_name(player_tag):
    player_info = get_player_info(player_tag)
    if player_info and 'club' in player_info:
        club_tag = player_info['club'].get('tag')
        if club_tag:
            club_info = get_club_info(club_tag)
            if club_info:
                return club_info.get('name', 'Unknown club name')
        return "Player is not in a club"
    return "Could not retrieve player information"
"""
def save_data(data, player_tag):
    filename = f"player_{player_tag.lstrip('#')}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_data(player_tag):
    filename = f"player_{player_tag.lstrip('#')}.json"
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return 'File Not found'
    except Exception as e:
        return f'Error: {e}'
"""

def get_all_player_data(player_tag):
    player_info = get_player_info(player_tag)
    player_battles = get_battles(player_tag)
    club_name = get_player_club_name(player_tag)
    
    existing_data = load_data(player_tag=player_tag) or {}
    updated_data = update_battle_archive(existing_data, player_battles)
    
    data = {
        "player_info": player_info,
        "recent_battles": player_battles,
        "battle_archive": updated_data['battle_archive'],
        "club_name": club_name,
        "last_updated": datetime.now().isoformat()
    }
    return data

if 'name' == '__main__':
    # Test the functions
    player_tag = '#GQROVLUOG'
    #print("Testing get_player_info:")
    #get_player_info(player_tag)
    print("\nTesting get_battles:")
    print(f'BATTLES: \n{get_battles(player_tag)}')

