import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
from matplotlib import style


style.use('fivethirtyeight')

df = pd.DataFrame()

def cubs_stats():
	cubs_stats = pd.read_html('http://www.espn.com/mlb/team/stats/batting/_/name/chc/chicago-cubs')
	for cub in cubs_stats:
		return cub[2:].convert_objects(convert_numeric=True)
		

df = cubs_stats()
df=df.rename(columns={0:'Name',1:'GP',2:'AB',3:'R',4:'H',5:'2B',6:'3B',7:'HR',8:'RBI',
	9:'TB',10:'BB',11:'SO',12:'SB',13:'BA',14:'OBP',15:'SLG',16:'OPS',17:'OWAR'})
df.set_index("Name", inplace=True)
df.dropna(inplace=True)

df['TB'].plot()
plt.show()


#df['GP'][1:].plot(ax=ax1)
#plt.show()