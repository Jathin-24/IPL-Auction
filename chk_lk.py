import pandas as pd

try:
    df = pd.read_excel('IPL_LIVE_AUCTION_TRACKER.xlsx', sheet_name='SOLD_HISTORY')
    print("ALL SOLD TO LUCKNOW:")
    lucknow = df[df['Team'].str.contains('Lucknow', na=False, case=False)]
    print(lucknow)
    print("\nTOTAL LUCKNOW:", len(lucknow))
    
    print("\nALL LUCKNOW TEAM SHEET:")
    luck_sheet = pd.read_excel('IPL_LIVE_AUCTION_TRACKER.xlsx', sheet_name='Lucknow Super Gaints')
    print(luck_sheet)
    print("\nTOTAL in TEAM SHEET:", len(luck_sheet))
except Exception as e:
    print(e)
