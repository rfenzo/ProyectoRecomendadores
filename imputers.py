import pandas as pd
import numpy as np
from fancyimpute import KNN, NuclearNormMinimization, SoftImpute, IterativeImputer, BiScaler

train = pd.read_csv('sparsed/train_subset_sparse.csv')

# X is the complete data matrix
# train has the same values as X except a subset have been replace with NaN

# Model each feature with missing values as a function of other features, and
# use that estimate for imputation.
X_filled_ii = IterativeImputer().fit_transform(train)

# Use 3 nearest rows which have a feature to fill in each row's missing features
X_filled_knn = KNN(k=3).fit_transform(train)

np.savetxt("sparsed/ii_impute.csv", X_filled_ii, delimiter=",")
np.savetxt("sparsed/knn_impute.csv", X_filled_knn, delimiter=",")
