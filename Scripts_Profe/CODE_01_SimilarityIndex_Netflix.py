import pandas as pd
import numpy as np
import sklearn.metrics as skm # similarity metrics
import scipy.spatial.distance as sc # distance metrics

# Import data
file_path = 'Test de películas (anónimo)(1-12).xlsx'
# data = pd.read_excel(file_path,encoding='latin_1',index_col=0) #old versions
data = pd.read_excel(file_path,index_col=0)
data.head()

# Select columns
def select_columns(x):
  csel = np.arange(9,246,3)
  users1 = list(x.iloc[:,6])
  cnames1 = list(x.columns.values[csel])
  x = x[cnames1]
  x.index = users1
  #x[np.isnan(x)]=0
  return x

datan =  select_columns(data)
datan.head()

def select_columnsNotSeen(x):
  csel = np.arange(9,246,3)
  users1 = list(x.iloc[:,6])
  cnames1 = list(x.columns.values[csel])
  x = x[cnames1]
  x.index = users1
  x[np.isnan(x)]=-1
  return x

datanotSeen =  select_columnsNotSeen(data)

# Average rating of the movies
movie_prom = datan.mean(axis=0)
user_prom = datan.mean(axis=1)

# Change the stars to like or dislike
cnames = list(datan.columns.values)
fnames = np.array(datan.index)
for col in cnames:
    datan[col]=np.where(datan[col]>3,1,0)
datan.head()
    

# Calculate similarity indices in users by sklearn
cf_m = skm.confusion_matrix(datan.iloc[0,:],datan.iloc[1,:])

sim_simple = skm.accuracy_score(datan.iloc[0,:],datan.iloc[1,:])
#sim_simple_new = (cf_m[0,0]+cf_m[1,1])/np.sum(cf_m)
print('Simple : %0.4f'%sim_simple)

sim_jac = skm.jaccard_score(datan.iloc[0,:],datan.iloc[1,:])
#sim_jac = (cf_m[0,0])/(np.sum(cf_m)-cf_m[1,1])
print('Jaccard: %0.4f'%sim_jac)

# Tip for those who have a different syntax
# conda update sklearn

# Calculation of distances by scipy
# https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
d1 = sc.euclidean(datan.iloc[0,:],datan.iloc[5,:])
print('Simple : %0.4f'%d1)
d2 = sc.canberra(datan.iloc[0,:],datan.iloc[5,:])
print('canberra: %0.4f'%d2)

# Calculate all possible combinations by scipy
D1 = sc.pdist(datan,'matching')
D1 = sc.squareform(D1)

D2 = sc.pdist(datan,'jaccard')
D2 = sc.squareform(D2)

# Select a user and determine the other most similar user
user = 1
D_user = D1[user]
D_user_sort = np.sort(D_user)
indx_user = np.argsort(D_user)


# Recommendation version 1. The most similar user
User = datan.loc[fnames[user]]
User_sim = datan.loc[fnames[indx_user[1]]]

indx_recomen = (User_sim ==1)&(User==0)
recomend1 = list(User.index[indx_recomen])
print('\n Movie list recommended:\n')
print(recomend1)


# Recommendation version 1.2. The most similar user
User = datanotSeen.loc[fnames[user]]
User_sim = datan.loc[fnames[indx_user[1]]]

indx_recomen = (User_sim ==1)&(User==-1)
recomend1 = list(User.index[indx_recomen])
print('\n Movie list recommended:\n')
print(recomend1)

