
# coding: utf-8

# In[31]:

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
import plotly
from plotly.graph_objs import *
import plotly.figure_factory as ff


# In[34]:

# import data
test = pd.read_csv('include/test.csv')
train = pd.read_csv('include/train.csv')
y = train['Survived']

def preprocess_data(dataframe):
    # drop unneeded columns
    dataframe.drop(dataframe.columns[[0, 1, 3, 8, 10, 11]], axis=1, inplace=True)
    # Get cabin letter
#     cabins = ['A', 'B', 'C', 'D', 'E', 'F', 'T', 'G']
#     dataframe['Cabin'] = dataframe['Cabin'].map(lambda x: substrings_in_string(x, cabins))
    enc = LabelEncoder()
#     dataframe['Cabin'] = enc.fit_transform(dataframe['Cabin'])
    dataframe['Sex'] = enc.fit_transform(dataframe['Sex'])
    dataframe['Sex'].fillna(0, inplace=True)
    dataframe['Age'].fillna(0, inplace=True)
    return dataframe


# taken from
# https://triangleinequality.wordpress.com/2013/09/08/basic-feature-engineering-with-the-titanic-data/
def substrings_in_string(big_string, substrings):
    for substring in substrings:
        if str(big_string).find(substring) != -1:
            return substring
    return np.nan


train = preprocess_data(train)
train = StandardScaler().fit_transform(train);
pca = PCA(n_components = 2)
train_2d = pca.fit_transform(train)
print(train_2d)


# In[30]:
traces = []
for name in (0, 1):
    trace = Scatter(
        x=train_2d[y==name,0],
        y=train_2d[y==name,1],
        mode='markers',
        name=name,
        marker=Marker(
            size=12,
            line=Line(
                color='rgba(217, 217, 217, 0.14)',
                width=0.5),
            opacity=0.8))
    traces.append(trace)

data = Data(traces)
layout = Layout(xaxis=XAxis(title='PC1', showline=False),
                yaxis=YAxis(title='PC2', showline=False))
fig = Figure(data=data, layout=layout)


# In[ ]:




# In[ ]:
