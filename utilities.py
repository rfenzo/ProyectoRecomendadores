import json
import pandas as pd

def dict2file(dictionary, filename):
  with open(filename, 'w') as f:
    json.dump(dictionary, f)

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

def sparse2Original():
  sparse = pd.read_csv('imputers/ii_impute.csv', header=None, index_col=0)

  columns = [0,'level_0','rating']
  renameColumns = {0:'user_id','level_0':'item_id'}
  original = sparse.unstack().reset_index(name = 'rating')[columns]
  original = original.rename(index=str, columns=renameColumns)
  original = original.sort_values(by=['user_id','item_id'])
  original.to_csv('imputers/ii_impute_not_sparse.csv', index=False)
