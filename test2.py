#%%
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import matplotlib as mpl
mpl.__version__
# '1.5.0'

import numpy as np
np.__version__
# '1.10.1'

import pandas as pd
pd.__version__
# u'0.17.0'

#%%
df = pd.read_csv('data/data.csv', index_col=0, header=[0, 1, 2], skiprows=[0], encoding='shift-jis')

#%%
df.head()
#df = df.iloc[:, [0, 3, 6]]
df.columns = [u'横浜', u'神戸', u'大阪', u'東広島', u'呉']
df.index = pd.to_datetime(df.index)
df.head()