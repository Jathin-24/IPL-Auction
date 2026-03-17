import pandas as pd
try:
    df = pd.read_excel('IPL LIST.xlsx')
    with open('columns.txt', 'w') as f:
        f.write(','.join(df.columns.tolist()))
        f.write('\n')
        f.write(df.head(5).to_csv())
except Exception as e:
    with open('error.txt', 'w') as f:
        f.write(str(e))
