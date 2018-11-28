import json

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
