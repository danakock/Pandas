import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

df = pd.read_csv('NCES-DROPOUT_RACE.csv')
print(df)

df.plot()
plt.show()