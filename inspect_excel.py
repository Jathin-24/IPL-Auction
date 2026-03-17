import pandas as pd

try:
    df = pd.read_excel('IPL LIST.xlsx')
    print(df.head())
    print(df.columns)
except Exception as e:
    print(e)
