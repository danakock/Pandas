import quandl
import pandas as pd
api_key = open('poorly_delimited.txt', 'r').read()
df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
df.columns = ["United States"]
print(df)