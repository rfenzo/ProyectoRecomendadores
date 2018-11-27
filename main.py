import pandas as pd
import numpy as np
from scipy import sparse

train = pd.read_csv('dataset/train.csv')

train_subset = train.loc[train['user_id'] < 5400]

#sparse = train.pivot(index='user_id', columns='item_id', values='rating')
#sparse.to_csv('dataset/train_sparse.csv')

sparse = train_subset.pivot(index='user_id', columns='item_id', values='rating')
sparse.to_csv('dataset/train_subset_sparse.csv')

#print(sparse)
