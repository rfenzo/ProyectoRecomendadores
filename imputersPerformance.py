import pandas as pd
import numpy as np
from utilities import file2dict, MAE, RMSE

test = file2dict('test.json')
test.pop('5400')

for i in ['knn','ii']:
  print(i)
  impute = pd.read_csv(f'imputers/{i}_impute.csv', header=None, index_col=0)
  MAES = []
  RMSES = []
  for user in test.keys():
    ratedSongs = [int(j)-1 for j in test[user].keys()]
    impute.index = np.arange(1, len(impute) + 1)
    imputed = impute.iloc[int(user)-1,ratedSongs]
    MAES.append(MAE(imputed, test[user].values()))
    RMSES.append(RMSE(imputed, test[user].values()))

  print('mae', np.mean(MAES))
  print('rmse', np.mean(RMSES))
  print()


