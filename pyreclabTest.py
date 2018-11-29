import pyreclab
from datetime import datetime as dt
import sys

models = {
  'userknn': pyreclab.UserKnn,
  'itemknn': pyreclab.ItemKnn, 
  'svd': pyreclab.SVD,
  'slopeone': pyreclab.SlopeOne,
}

def generateModel(trainFile, modelName):
  params = {
    'dataset': trainFile,
    'dlmchar': b',',
    'header': True,
    'usercol': 0,
    'itemcol': 1,
  }
  if modelName in ['als','alscg']:
    params['observationcol'] = 2 
  else:
    params['ratingcol'] = 2

  return models[modelName](**params)

def trainModel(model, *args):
  if len(args):
    return model.train(*args)
  return model.train()

def testModel(model, testFile):
  _, MAE, RMSE = model.test(input_file = testFile,
                            dlmchar = b',',
                            header = True,
                            usercol = 0,
                            itemcol = 1,
                            ratingcol = 2)
  return MAE, RMSE

def runTest(trainFile, testFile, modelName, params):
  model = generateModel(trainFile, modelName)
  trainModel(model, *params)
  MAE, RMSE = testModel(model, testFile)

  with open('results.txt','a') as f:
    output = f'{modelName} ({params}), MAE {MAE}, RMSE {RMSE}\n'
    print(output)
    f.write(output)

trainFile = 'longAndFilteredImputed/ii.csv'
testFile = 'dataset/test.csv'

tests = []

# svd
for f in [500,1000]:
  for m in [50,100]:
    for lr in [0.01,0.05]:
      for lamb in [0.1,0.5]:
        tests.append((trainFile, testFile, 'svd', [f,m,lr,lamb]))
        continue

# userknn & itemknn
for i in [2,5,10]:
  for m in ['pearson','cosine']:
    #tests.append((trainFile, testFile, 'userknn', [i,m]))
    #tests.append((trainFile, testFile, 'itemknn', [i,m]))
    continue

# slopeone
#tests.append((trainFile, testFile, 'slopeone', []))

for t in tests:
  runTest(*t)
