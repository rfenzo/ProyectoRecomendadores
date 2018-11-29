import pandas as pd
import numpy as np
from utilities import file2dict, MAE, RMSE, sparse2long

test = file2dict('test.json')

def values1to5(df):
  df.loc[df['rating']<1, ['rating']] = 1
  df.loc[df['rating']>5, ['rating']] = 5
  return df

def evaluate(folder):
  for i in ['ii','knn2','knn5','knn10','knn20']:
    impute = pd.read_csv(f'{folder}/{i}.csv').groupby('user_id')
    MAES = []
    RMSES = []
    for user in test.keys():
      ratedSongs = [int(j) for j in test[user].keys()]
      group = impute.get_group(1)
      imputed = group[group['item_id'].isin(ratedSongs)]['rating'].tolist()
      MAES.append(MAE(imputed, test[user].values()))
      RMSES.append(RMSE(imputed, test[user].values()))

    with open('results.txt','a') as f:
      output = f'imputed {i}, MAE {np.mean(MAES)}, RMSE {np.mean(RMSES)}\n'
      print(output)
      f.write(output)

def filter(fileName, destination):
  raw_imputes = pd.read_csv(fileName)
  impute = values1to5(raw_imputes).round()
  impute.to_csv(destination, index=False)

# filter('longImputed/ii.csv', 'longAndFilteredImputed/ii.csv')
# filter('longImputed/knn2.csv', 'longAndFilteredImputed/knn2.csv')
# filter('longImputed/knn5.csv', 'longAndFilteredImputed/knn5.csv')
# filter('longImputed/knn10.csv', 'longAndFilteredImputed/knn10.csv')
# filter('longImputed/knn20.csv', 'longAndFilteredImputed/knn20.csv')

evaluate('longAndFilteredImputed')
