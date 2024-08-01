import json
from datetime import datetime

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
        return None

def is_data_fresh(data, max_age_days=1):
    if not data or 'last_updated' not in data:
        return False
    last_updated = datetime.fromisoformat(data['last_updated'])
    return (datetime.now() - last_updated).days < max_age_days

def update_battle_archive(existing_data, new_battles):
    if 'battle_archive' not in existing_data:
        existing_data['battle_archive'] = []
    
    existing_battle_ids = set(battle['battleTime'] for battle in existing_data['battle_archive'])
    
    for battle in new_battles['items']:  # Change this line
        if battle['battleTime'] not in existing_battle_ids:
            existing_data['battle_archive'].append(battle)
            existing_battle_ids.add(battle['battleTime'])
    
    existing_data['battle_archive'].sort(key=lambda x: x['battleTime'], reverse=True)
    return existing_data
        