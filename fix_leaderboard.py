import pandas as pd

EXCEL_FILE = 'IPL_LIVE_AUCTION_TRACKER_Day_2.xlsx'

try:
    xl = pd.ExcelFile(EXCEL_FILE)
    sheets = xl.sheet_names

    # Read the existing leaderboard to get the Starting Budget for each team
    try:
        current_lb = pd.read_excel(xl, sheet_name='LEADERBOARD')
        budgets = dict(zip(current_lb['Team Name'], current_lb['Starting Budget']))
    except:
        print("Could not read existing Leaderboard to get Starting Budgets. Using default 200.")
        budgets = {}

    leaderboard_data = []
    processed_teams = set()

    # Process all existing team sheets
    team_sheets = [s for s in sheets if s not in ['LEADERBOARD', 'SOLD_HISTORY', 'UNSOLD_PLAYERS']]
    for team in team_sheets:
        df = pd.read_excel(xl, sheet_name=team)
        # Check if 'Price Paid' column exists
        coins_spent = df['Price Paid'].sum() if 'Price Paid' in df.columns else 0
        players_bought = len(df)
        initial_budget = budgets.get(team, 200)
        
        leaderboard_data.append({
            'Team Name': team,
            'Starting Budget': initial_budget,
            'Coins Spent': coins_spent,
            'Current Balance': initial_budget - coins_spent,
            'Players Bought': players_bought
        })
        processed_teams.add(team)

    # Re-add any teams that were in the original Leaderboard but don't have a team sheet
    for team, init_b in budgets.items():
        if team not in processed_teams:
            leaderboard_data.append({
                'Team Name': team,
                'Starting Budget': init_b,
                'Coins Spent': 0,
                'Current Balance': init_b,
                'Players Bought': 0
            })

    # Create the new Leaderboard DataFrame
    df_lb = pd.DataFrame(leaderboard_data)

    # Replace the LEADERBOARD sheet in the existing Excel file
    with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df_lb.to_excel(writer, sheet_name='LEADERBOARD', index=False)

    print(f"Successfully rewritten the 'LEADERBOARD' sheet based on individual team sheets ({len(team_sheets)} teams).")

except Exception as e:
    print(f"Error repairing Excel file: {e}")
