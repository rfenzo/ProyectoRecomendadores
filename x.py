import pandas as pd

test = pd.read_csv('dataset/test.csv')
train_subset = pd.read_csv('dataset/train_subset_sparse.csv')
print(train_subset.shape)
print(test.groupby('user_id')['item_id'].get_group(1))


