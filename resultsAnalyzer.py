from matplotlib import pyplot as plt
import numpy as np
# best svd
# 1000, 100, 0.01, 0.1
# MAE 1.18171799776724
# RMSE 1.4070925220270825

# slope one
# MAE 1.2080686933891533
# RMSE 1.4928512277529637

userknn = [
  (2, 'pearson', 1.4077470259303348, 1.7407936109164308),
  (2, 'cosine', 1.233188818718428, 1.5542508906169898),
  (5, 'pearson', 1.3060009769779901, 1.6038562310627837),
  (5, 'cosine', 1.1358310244746366, 1.428017137259123),
  (10, 'pearson', 1.2887057864499432, 1.5809249628046513),
  (10, 'cosine', 1.1799083226038636, 1.4691141102593357),
]

itemknn = [
  (2, 'pearson', 1.366707372432426, 1.719325407271569),
  (2, 'cosine', 1.2831811626942065, 1.6286756244189167),
  (5, 'pearson', 1.2848096604533692, 1.5975636306937215),
  (5, 'cosine', 1.2205544707073859, 1.5228163832531965),
  (10, 'pearson', 1.2726424332263173, 1.5688882556477926),
  (10, 'cosine', 1.2327071860179888, 1.5249863900456964),
]

imputed = {
  'ii': (1.38032, 1.6750920556784956),
  'knn2': (1.6109799999999999, 2.050157996406077),
  'knn5': (1.5686799999999999, 1.9883387732542934),
  'knn10': (1.5621200000000002, 1.9775907724702366),
  'knn20': (1.56176, 1.9744592623624329),
}

def graphKnn():
  ylabel = ['MAE','RMSE']
  for i in [2,3]:
    ax = plt.subplot(1,2,i-1)
    ax.set_title(ylabel[i-2]+' vs Neighbors', fontsize= 18)
    plt.tight_layout(pad=4)
    userknnplot = [(x[0],x[i]) for x in userknn if x[1]=='pearson']
    x,y = zip(*userknnplot)
    plt.plot(x,y, label = "UserKnn\n(pearson)")

    itemknnplot = [(x[0],x[i]) for x in itemknn if x[1]=='cosine']
    x,y = zip(*itemknnplot)
    plt.plot(x,y, label = "ItemKnn\n(cosine)")
    plt.ylabel(ylabel[i-2], fontsize=15)
    plt.xlabel('Neighbors', fontsize=15)
    plt.yticks(fontsize=15)
    plt.xticks(fontsize=15)
    plt.legend(fontsize=15)
  plt.show()
  plt.gcf().clear()



# Create data
 
data = (imputed.values())
colors = ("red", "green", "blue", "black", "yellow")
groups = ("Iterative Imputer", "KNN-2", "KNN-5", "KNN-10", "KNN-20") 
 
# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
 
for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=150, label=group)
 
plt.title('Desempeño Imputers',fontsize=15)
plt.xlabel('MAE', fontsize=15)
plt.ylabel('RMSE', fontsize=15)
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.legend( fontsize=15)
plt.show()
