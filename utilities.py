import json
import pandas as pd
import os
import pprint

def dict2file(dictionary, filename):
  with open(filename, 'w') as f:
    json.dump(dictionary, f, indent = 2)

def file2dict(filename):
  with open(filename, 'r') as f:
    return json.load(f)

def test2dict(test):
  users = test.groupby("user_id")
  test = {}
  for user in users.groups.keys():
      test[user] = {}
      for i in range(len(users["item_id"].get_group(user))):
          test[user][users["item_id"].get_group(user).tolist()[i]] = users["rating"].get_group(user).tolist()[i]
  return test

def MAE(list1, list2):
  suma = 0
  for a,b in zip(list1,list2):
    suma += abs(a-b)
  return suma/len(list1)

def RMSE(list1,list2):
  suma = 0
  for a,b in zip(list1,list2):
    suma += (a-b)**2
  return (suma/len(list1))**0.5

def sparse2long(filepath, destination):
  sparse = pd.read_csv(filepath, header=None, index_col=0)
  columns = [0,'level_0','rating']
  renameColumns = {0:'user_id','level_0':'item_id'}
  long = sparse.unstack().reset_index(name = 'rating')[columns]
  long = long.rename(index=str, columns=renameColumns)
  long = long.sort_values(by=['user_id','item_id'])
  long.to_csv(destination, index=False)

def shutdown():
  os.system("shutdown now -h")

# sparse2long('imputed/knn2.csv', 'longImputed/knn2.csv')
# sparse2long('imputed/knn5.csv', 'longImputed/knn5.csv')
# sparse2long('imputed/knn10.csv', 'longImputed/knn10.csv')
# sparse2long('imputed/knn20.csv', 'longImputed/knn20csv')
