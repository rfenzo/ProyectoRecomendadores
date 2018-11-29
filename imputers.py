import pandas as pd
import numpy as np
from fancyimpute import KNN, NuclearNormMinimization, SoftImpute, IterativeImputer, BiScaler, IterativeSVD, BiScaler

train = pd.read_csv('sparsed/training_10000_sparse.csv')

# Model each feature with missing values as a function of other features, and
# use that estimate for imputation.

#ii = IterativeImputer().fit_transform(train)
#np.savetxt("imputed/ii_subset_impute.csv", ii, delimiter=",")

# Use 3 nearest rows which have a feature to fill in each row's missing features

# knn2 = KNN(k=2).fit_transform(train)
# np.savetxt("imputed/knn2.csv", knn2, delimiter=",")


#knn5 = KNN(k=5).fit_transform(train)
#np.savetxt("imputed/knn5_impute.csv", knn5, delimiter=",")

#knn10 = KNN(k=10).fit_transform(train)
#np.savetxt("imputed/knn10_impute.csv", knn10, delimiter=",")

#knn20 = KNN(k=20).fit_transform(train)
#np.savetxt("imputed/knn20_impute.csv", knn20, delimiter=",")


