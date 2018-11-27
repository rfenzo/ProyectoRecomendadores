import pandas as pd
import numpy as np
from scipy import sparse

train = pd.read_csv('dataset/train.csv')
sparse = train.pivot(index='user_id', columns='item_id', values='rating')
sparse.to_csv('train_sparse.csv')

