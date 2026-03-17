import pandas as pd
import json

try:
    df = pd.read_excel('IPL LIST.xlsx')
    # Use standard column names based on user description
    # Mapping likely columns: S.No/SNo -> sno, Player Name/Name -> name, Role -> role, Points -> points, Coins/Base Price -> base
    
    def find_col(candidates):
        for c in df.columns:
            if c.lower().strip() in candidates:
                return c
        return None

    sno_col = find_col(['sno', 's.no', 'sr.no', 'id', 'serial', 'serial no', 'no'])
    name_col = find_col(['name', 'player', 'player name', 'full name', 'players'])
    role_col = find_col(['role', 'position', 'type'])
    points_col = find_col(['points', 'role points', 'rp', 'score'])
    coins_col = find_col(['coins', 'base price', 'price', 'base', 'budget'])

    players = []
    for _, row in df.iterrows():
        players.append({
            'sno': row[sno_col] if sno_col else 0,
            'name': row[name_col] if name_col else 'Unnamed',
            'role': row[role_col] if role_col else 'N/A',
            'points': row[points_col] if points_col else 0,
            'base': row[coins_col] if coins_col else 0,
            'status': 'available',
            'soldTo': None,
            'soldPrice': 0
        })

    with open('players_data.js', 'w') as f:
        f.write("const PRELOADED_PLAYERS = " + json.dumps(players) + ";")
    print("SUCCESS")
except Exception as e:
    with open('players_data.js', 'w') as f:
        f.write("const PRELOADED_PLAYERS = []; // Error: " + str(e))
    print("ERROR: " + str(e))
