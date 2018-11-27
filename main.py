import pandas as pd
import numpy as np
from scipy import sparse

train = pd.read_csv('dataset/train.csv')

mat = sparse.coo_matrix((train["rating"], (train["user_id"], train["item_id"])))
dense_mat = mat.todense()
x = np.delete(dense_mat,0,0)
x = np.delete(x,0,1)
np.savetxt("train_sparse.csv", x, delimiter=",")


