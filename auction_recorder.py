import http.server
import json
import pandas as pd
import os
import sys
from datetime import datetime

# PORT 5000 is used by the HTML dashboard to send data
PORT = 5000
EXCEL_FILE = 'IPL_LIVE_AUCTION_TRACKER_Day_2.xlsx'

latest_state = {}

class AuctionHandler(http.server.BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        if self.path == '/sync':
            global latest_state
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            latest_state = data
            self.save_to_excel(data)
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'synced'}).encode('utf-8'))

    def do_GET(self):
        if self.path == '/state':
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(latest_state).encode('utf-8'))

    def save_to_excel(self, data):
        try:
            teams = data.get('teams', [])
            players = data.get('players', [])
            sold_players = [p for p in players if p.get('status') == 'sold']
            unsold_players = [p for p in players if p.get('status') == 'unsold']
            
            leaderboard = []
            for t in teams:
                team_picks = [p for p in sold_players if p.get('soldTo') == t['name']]
                coins_spent = sum(int(p.get('soldPrice', 0)) for p in team_picks)
                
                leaderboard.append({
                    'Team Name': t['name'],
                    'Starting Budget': t['initialBudget'],
                    'Coins Spent': coins_spent,
                    'Current Balance': t['initialBudget'] - coins_spent,
                    'Players Bought': len(team_picks)
                })
            df_leaderboard = pd.DataFrame(leaderboard)
            df_sold = pd.DataFrame(sold_players)
            df_unsold = pd.DataFrame(unsold_players)
            
            try:
                with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl') as writer:
                    df_leaderboard.to_excel(writer, sheet_name='LEADERBOARD', index=False)
                    if not df_sold.empty:
                        cols = ['sno', 'name', 'role', 'points', 'soldTo', 'soldPrice']
                        df_sold[cols].rename(columns={'sno':'S.No', 'soldTo':'Team', 'soldPrice':'Price'}).to_excel(writer, sheet_name='SOLD_HISTORY', index=False)
                    if not df_unsold.empty:
                        df_unsold[['sno', 'name', 'role', 'base']].to_excel(writer, sheet_name='UNSOLD_PLAYERS', index=False)
                    for t in teams:
                        team_picks = [p for p in sold_players if p.get('soldTo') == t['name']]
                        if team_picks:
                            df_team = pd.DataFrame(team_picks)[['sno', 'name', 'role', 'soldPrice']]
                            df_team.rename(columns={'sno':'S.No', 'soldPrice':'Price Paid'}).to_excel(writer, sheet_name=t['name'][:30], index=False)
                print(f"[{datetime.now().strftime('%H:%M:%S')}] SYNC SUCCESS: {EXCEL_FILE} updated.", flush=True)
            except PermissionError:
                print(f"!!! SYNC FAILED: Please close '{EXCEL_FILE}' in Excel!", flush=True)
        except Exception as e:
            print(f"SAVE ERROR: {e}", flush=True)

if __name__ == '__main__':
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, AuctionHandler)
    with open('RUNNING.txt', 'w') as f: f.write('SERVER_READY')
    print("="*50, flush=True)
    print(f"IPL AUCTION LIVE SYNC SERVER ACTIVE ON PORT {PORT}", flush=True)
    print(f"Updating: {os.path.abspath(EXCEL_FILE)}", flush=True)
    print("="*50, flush=True)
    httpd.serve_forever()
