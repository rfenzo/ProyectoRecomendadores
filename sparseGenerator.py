import pandas as pd
from utilities import test2dict, dict2file


training = pd.read_csv('dataset/training.csv')
test = pd.read_csv('dataset/test.csv')

# to create test.json
# dict2file(test2dict(test), 'test.json')

# to create train.json
# dict2file(test2dict(training), 'train.json')

sparse = training.pivot(index='user_id', columns='item_id', values='rating')
sparse.to_csv('sparsed/training_sparse.csv')
