import pandas as pd
import numpy as np
from scipy import sparse
from fancyimpute import KNN, NuclearNormMinimization, SoftImpute, IterativeImputer, BiScaler

train = pd.read_csv('dataset/train_subset_sparse.csv')
test = pd.read_csv('dataset/test.csv')


# X is the complete data matrix
# train has the same values as X except a subset have been replace with NaN

# Model each feature with missing values as a function of other features, and
# use that estimate for imputation.
X_filled_ii = IterativeImputer().fit_transform(train)

# Use 3 nearest rows which have a feature to fill in each row's missing features
#X_filled_knn = KNN(k=3).fit_transform(train)

# matrix completion using convex optimization to find low-rank solution
# that still matches observed values. Slow!
#X_filled_nnm = NuclearNormMinimization().fit_transform(train)

# Instead of solving the nuclear norm objective directly, instead
# induce sparsity using singular value thresholding
#train_normalized = BiScaler().fit_transform(train)
#X_filled_softimpute = SoftImpute().fit_transform(train_normalized)

print(type(X_filled_ii))
np.savetxt("knn_impute.csv", X_filled_ii, delimiter=",")














# users = test.groupby("user_id")
# compare = {}
# for user in users.groups.keys():
#     compare[user] = {}
#     for i in range(len(users["item_id"].get_group(user))):
#         compare[user][users["item_id"].get_group(user).tolist()[i]] = users["rating"].get_group(user).tolist()[i]
#     print(compare[user])

