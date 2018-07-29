#%%
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import matplotlib as mpl
mpl.__version__

import numpy as np
np.__version__

import pandas as pd
pd.__version__

#%%
df = pd.read_csv('data/data.csv', index_col=0, header=[0, 1, 2], skiprows=[0], encoding='shift-jis')

#%%
df.head()
#df = df.iloc[:, [0, 3, 6]]
df.columns = [u'横浜', u'神戸', u'大阪', u'東広島', u'呉']
df.index = pd.to_datetime(df.index)
df.head()

#%%
df.plot()

monthly = df.groupby(pd.Grouper(level=0, freq='M')).mean()
monthly

monthly.plot.bar(color=['#348ABD', '#7A68A6', '#A60628'])

#%%
monthly.index.format()
# ['2014-01-31', '2014-02-28', '2014-03-31', '2014-04-30', '2014-05-31', '2014-06-30',
#  '2014-07-31', '2014-08-31', '2014-09-30', '2014-10-31', '2014-11-30', '2014-12-31']
monthly.index = monthly.index.format()
monthly.plot.bar(color=['#348ABD', '#7A68A6', '#A60628'])

#%%
monthly.plot.bar(cmap='rainbow')

#%%
ax = monthly[u'横浜'].plot(legend=True)
monthly[[u'神戸', u'大阪', u'東広島', u'呉']].plot.bar(ax=ax, rot=30)

#%%
#fig = plt.figure()
#ax = fig.add_axes([0.1, 0.1, 0.9, 0.9], polar=True)
#indexer = np.arange(1, 13) * 2 * np.pi / 12
#monthly.index = indexer
#monthly.append(monthly.iloc[0]).plot(ax=ax)
#ax.set_xticks(indexer)
#ax.set_xticklabels(np.arange(1, 13))

#%%
df.plot.hist(bins=100, alpha=0.5)

#%%
#fig, axes = plt.subplots(4, 3, figsize=(8, 6))
#plt.subplots_adjust(wspace=0.5, hspace=0.5)
#for (ax, (key, group)) in zip(axes.flatten(), df.groupby(pd.Grouper(level=0, freq='M'))):
#    ax = group.plot.kde(ax=ax, legend=False, fontsize=8)
#    ax.set_ylabel('')
#    ax.set_title(key, fontsize=8)

#%%
fig, axes = plt.subplots(4, 3, figsize=(8, 6))
plt.subplots_adjust(wspace=0.5, hspace=0.5)
for (ax, (key, group)) in zip(axes.flatten(), df.groupby(pd.Grouper(level=0, freq='M'))):
    ax = group.plot.box(ax=ax)
    ax.set_ylabel('')
    ax.set_title(key, fontsize=8)

#%%
df.plot(kind='scatter', x=u'横浜', y=u'神戸')

#%%
df.plot(kind='scatter', x=u'横浜', y=u'神戸', c=df.index.month, cmap='winter')

#%%
cmap = plt.get_cmap('rainbow')
colors = [cmap(c / 12.0) for c in np.arange(1, 13)]
colors
# [(0.33529411764705885, 0.25584277759443558, 0.99164469551074275, 1.0),
#  (0.17058823529411765, 0.49465584339977881, 0.96671840426918743, 1.0),
#  ...
#  (1.0, 0.25584277759443586, 0.12899921653020341, 1.0),
#  (1.0, 1.2246467991473532e-16, 6.123233995736766e-17, 1.0)]

fig, ax = plt.subplots(1, 1)
for i, (key, group) in enumerate(df.groupby(pd.Grouper(level=0, freq='M')), start=1):
    group.plot(kind='scatter', x=u'横浜', y=u'神戸', color=cmap(i / 12.0), ax=ax, label=i)

#%%
df['month'] = df.index.month
df.plot(kind='scatter', x='month', y=u'横浜')

#%%
df['month2'] = df.index.month + np.random.normal(loc=0, scale=0.05, size=len(df.index.month))
df.plot(kind='scatter', x='month2', y=u'横浜')

#%%
df2 = df.copy()
df2[u'横浜2'] = df2[u'横浜'] // 10 * 10 
df2['count'] = 1
df2 = df2.groupby(['month', u'横浜2'])['count'].count().reset_index()
df2.head()

#%%
df2.plot.scatter(x='month', y=u'横浜2', s=df2['count'] * 10)
df.plot(kind='scatter', x='month2', y=u'横浜')

#%%
#piv = pd.pivot_table(df, index=u'横浜2', columns=df.index.month, values=u'横浜', aggfunc='count')
#piv = piv.fillna(0)
#piv

#%%
#piv.pipe(plt.imshow, cmap='winter')
#ax = plt.gca()
#ax.invert_yaxis()
#ax.set_yticks(np.arange(4))
#ax.set_yticklabels(piv.index)
