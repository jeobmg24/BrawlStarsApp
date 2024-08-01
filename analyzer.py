from data_manager import load_data

def get_win_rate(player_tag, selection=None):
    """This function will get the win rate of the player based on the archives"""
    data = load_data(player_tag)
    battles = data.get('battle_archive', [])
    win = 0
    total = len(battles)
    for battle in battles:
        try:
            if battle['battle']['result'] == "victory":           
                win += 1
        except Exception as e:
            print(f'Battle not counted: {e}')
    return (win / total) * 100
    

def get_most_played_mode(player_tag):
    data = load_data(player_tag)
    battle_archive = data.get('battle_archive', [])
    
    mode_counts = {}
    for battle in battle_archive:
        mode = battle['event']['mode']
        mode_counts[mode] = mode_counts.get(mode, 0) + 1
    
    return max(mode_counts, key=mode_counts.get) if mode_counts else None
"""
def battles_with(player_tag, brawler):
    data = load_data(player_tag=player_tag)
    battles = data.get('battle_archive', [])
    
    matching = []
    for battle in battles:
        print(f'battle {battle} \n')
        try: #if the battle is a team battle
            wanted = battle['battle']['teams']
        except KeyError: # if teams do not exist in this game mode
            wanted = battle['battle']['players']
            for person in wanted:
                #print(f'person: {person}')
                for detail in person:
                    print(detail)
                    if detail['tag'] == player_tag and detail['brawlers']['name'] == brawler:
                        matching.append(battle)

        #print(f'\nWANTED: {wanted}')
            #if detail['tag'] == player_tag:
                #print(f'player {detail} \n')
    
    
    return matching
"""

def most_mvp(player_tag):
    data = load_data(player_tag=player_tag)
    battles = data.get('battle_archive', [])
    counting = dict()
    
    for battle in battles:
        battle_data = battle.get('battle', battle)
        
        star_player = battle_data.get('starPlayer')
        if star_player:
            id_tag = star_player['tag']
            id_tag = id_tag.strip().upper().replace('0', 'O')
            if id_tag == player_tag:
                brawler_name = star_player['brawler']['name']
                if brawler_name in counting.keys():
                    counting[brawler_name] += 1
                else:
                    counting[brawler_name] = 1
            
    
    return counting

def display_win_rate_brawler(username, brawler):
    """Calculates the win rate and amount of star Player awards brawler has gotten
        Inputs: username (tag of the player)
                brawler: brawler that is chosen in dropdown menu
        
        Outputs: List containing
                    1: win rate in percentage form
                    2: Total number of games played
                    3: Number of star Player awards recieved"""
    print(f"Analyzing for brawler: '{brawler}'")  # Debug print
    data = load_data(username)
    battles = data.get('battle_archive', [])
    wins = 0
    total = 0
    stars = 0
    
    for battle in battles:
        if battle['battle']['mode'] == 'soloShowdown':
            if battle['battle']['rank'] <= 4:
                wins += 1
            total += 1
        elif 'teams' in battle['battle']:
            try:
                star_player = battle['battle']['starPlayer']
                if star_player['tag'].strip().upper().replace('0', 'O') == username and star_player['brawler']['name'] == brawler.upper():
                    stars += 1
            except:
                continue # cannot find starPlayer key in this dictionary
            for team in battle['battle']['teams']:
                for player in team:
                    #print(f"Comparing '{player['brawler']['name']}' with '{brawler}'")  # Debug print
                    if player['brawler']['name'] == brawler:
                        total += 1
                        try:
                            if battle['battle']['result'] == 'victory':
                                wins += 1
                        except:
                            pass #this battle does not have wins
    
    #print(f"Total battles: {total}, Wins: {wins}")  # Debug print
    
    if total == 0:
        return f"No battles found for {brawler}"
    else:
        win_rate = (wins / total) * 100
        return f"{win_rate:.2f}%", total, stars
    


                
        

    
def best_map_brawler(username, brawler):
    data = load_data(username)
    battles = data.get('battle_archive', [])
    maps = {}
    for battle in battles:
        try:
            #print(battle)
            res = battle['battle']['result'] 
            if res == "victory":
                teams = battle['battle']['teams']
                for team in teams:
                    for player in team:
                        if player['brawler']['name'] == brawler and player['tag'].strip().upper().replace('0', 'O') == username:
                            mapp = battle['event']['map']
                            if mapp in maps.keys():
                                maps[mapp] += 1
                            else:
                                maps[mapp] = 1
        except Exception as e:
            pass
    print(maps)
    try:
        fav = max(maps, key=maps.get) # return the key with the highest value
    except Exception as e:
        return f"No battles played with this brawler: {e}"
        
    return fav
    
                
                
def display_win_rate_map(player_tag, chosen=None):
    """This function will output useful stats based on the players name and chosen field
        Input: player tag (str): uppercase letter tag special to the player
               chosen (str): the brawler, mode, or map chosen in the gui
        Output: Table signifying:
                TBD------"""
    data = load_data(player_tag=player_tag)
    battles = data.get('battle_archive', [])
    wins = 0
    total = 0
    
    for battle in battles:
        battle_data = battle['battle']
        #print(f'\n{battle}\n')
        try:
            result = battle_data['result']
            if result:
                mapp = battle['event']['map']
                if mapp == chosen:
                    if result == "victory": wins += 1
                    total += 1 
                             
        except Exception as e:
            print(f'Error: {e}')
    try:
        return f"win rate map: {((wins / total) * 100)}", total  
    except ZeroDivisionError:
        return "No games found with this selection"      
        
    
    
    
    
        
    

if __name__ == '__main__':
    print(display_win_rate_brawler('#GQROVLUOG', 'BROCK'))