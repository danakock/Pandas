import pandas as pd

df = pd.read_csv('ZILL-Z91655_3B.csv')
#print(df)

df.set_index('Date', inplace=True)
df.to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv', index_col=0)
#print(df.head())

df.columns = ['House Prices']
#print(df.head())

df.to_csv('newcsv3.csv')
# No Headers
df.to_csv('newcsv4.csv', header=False)
# Create Headers
df.to_csv('newcsv4.csv', names = ['Date', 'House_Price'], index_col=0)
#print(df.head())
# Convert to HTML
#df.to_html('example.html')

# Rename a column
df.rename(columns={'House Prices': 'Prices'}, inplace=True)
print(df)
