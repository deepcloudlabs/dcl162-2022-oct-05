import pandas as pd

df = pd.read_csv("employees_header.csv")
print(df.index)
print(df.columns)
print(df)