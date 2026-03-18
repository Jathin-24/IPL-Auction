import pandas as pd
try:
    xl = pd.ExcelFile('IPL LIST.xlsx')
    print(f"Sheets: {xl.sheet_names}")
    for sheet in xl.sheet_names:
        df = pd.read_excel(xl, sheet_name=sheet)
        print(f"\n--- Sheet: {sheet} ---")
        print(f"Columns: {df.columns.tolist()}")
        print("First 2 rows:")
        print(df.head(2))
except Exception as e:
    print(f"Error: {e}")
