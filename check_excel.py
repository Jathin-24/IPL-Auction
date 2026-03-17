import pandas as pd
try:
    df = pd.read_excel('IPL LIST.xlsx')
    with open('excel_info.txt', 'w') as f:
        f.write("COLUMNS: " + str(df.columns.tolist()) + "\n")
        f.write("FIRST_ROW: " + str(df.iloc[0].to_dict()) + "\n")
except Exception as e:
    with open('excel_info.txt', 'w') as f:
        f.write("ERROR: " + str(e))
