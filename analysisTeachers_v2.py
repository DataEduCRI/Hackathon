# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 15:22:26 2017

@author: iryna
"""

import pandas as pd
import os
#os.getcwd()
#os.chdir('/Users/iryna/dataOECD/ours') 
import matplotlib.pyplot
from scipy.stats.stats import pearsonr  

DB=pd.read_csv("OCDEfinal4_newcols.csv", index_col=0, sep=";")


"""
explicitVars=pd.read_excel("/Users/iryna/dataOECD/ours/RecodevT.xlsx")

len(DB.columns)
DB.columns[277]
DB.columns[277-31]
newcolumns=pd.concat([pd.DataFrame(DB.columns[0:(277-31)]),explicitVars.transpose(), pd.DataFrame(DB.columns[276:278]) ], axis=0, ignore_index=True)

newcolumns.transpose().to_csv("newcolumns.csv", sep=",", index=False)

DB.columns=newcolumns

"""

DB.head(1)
DB.index=DB['location']
DBTalis=DB.ix[:,len(DB.columns)-31:len(DB.columns)-2]
DBTalis.head(1)
DBTalis.index=DB['location']

"""
plt.plot(DBTalis['vTBelieveHelpStudentsThinkCritic'])

DBPisa=DB['reading2015']

plt.plot(DBTalis['vTBelieveHelpStudentsThinkCritic'],DB['science2015'], "bo")
plt.plot(DBTalis['vTFB2'],DB['science2015'], "bo")


fig, ax = plt.subplots()
plt.plot(DBTalis['vTFB2'], DB['science2015'], "bo")
index=pd.DataFrame(DBTalis['vTFB2'].index)
for i, index in enumerate(index.values):
    ax.annotate(index[0], (DBTalis['vTFB2'].iloc[i],DB['science2015'].iloc[i]))
 





DBTalis['vTBelieveHelpStudentsThinkCritic'].sort_values()

plt.plot(DBTalis['vTBelieveHelpStudentsValueLearning'],DB['science2015'], "bo")
DBTalis['vTBelieveHelpStudentsValueLearning'].sort_values()

#looks like a bad var: very small for best
plt.plot(DBTalis['vTProfDev'],DB['science2015'], "bo", )
DBTalis['vTProfDev'].sort_values()

#pearsonr(DBTalis['vTProfDev'],DB['science2015'] )

#
DBPT=pd.concat([DB['science2015'],DBTalis], axis=1)

rho = DBPT.corr('spearman')
DBTalisNoExtremes=DBTalis.drop(["Brazil","Mexico","Chile"])
DBPTNE=pd.concat([DB['science2015'],DBTalisNoExtremes], axis=1)
rho=DBPTNE.corr('pearson')

plt.plot(DB['science2015'], DBTalis['vTTime2'], "bo")

plt.plot(DB['science2015'], DBTalis['vTPercentCompleteTrain'], "bo")


#very bad completion of training in mexico
DBTalis['vTPercentCompleteTrain'].sort_values()

vtTimeTeaching
plt.plot(DB['science2015'], DBTalis['vtTimeTeaching'], "bo")

#try
fig, ax = plt.subplots()
plt.plot(DB['science2015'], DBTalis['vTTime2'], "bo")
#DBTalisIndex=np.array[DBTalis.index.values]

index=pd.DataFrame(DBTalis.index)
for i, index in enumerate(index.values):
    ax.annotate(index[0], (DB['science2015'].iloc[i],DBTalis['vTTime2'].iloc[i]))
    

"""    
 ####regression  
#Determiner des groupes de pays : ACP // ACM : profs.
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA as sklearnPCA


X = DBTalis
X= X.dropna()
X_std = StandardScaler().fit_transform(X)

sklearn_pca = sklearnPCA(n_components=3)
Y_sklearn = sklearn_pca.fit_transform(X_std)





fig, ax = plt.subplots()
plt.plot(Y_sklearn[:,0], Y_sklearn[:,1], "bo")

index=pd.DataFrame(X.index)
for i, index in enumerate(index.values):
    ax.annotate(index[0], (Y_sklearn[i,0],Y_sklearn[i,1]))
  
fig.savefig('PCATalis.eps', format='eps',bbox_inches = "tight", dpi=1000) #frameon=True, pad_inches=5  

"""

maxDBPisa=DBPisa.max()
minDBPisa=DBPisa.min()











color=[str(np.array((DBPisa[item]-minDBPisa)/(maxDBPisa-minDBPisa)) for item in X.index )]

fig, ax = plt.subplots()


plt.plot(Y_sklearn[:,0], Y_sklearn[:,1], "bo")






for i in DBPisa.index:
    print(i)    
    
    plt.plot(Y_sklearn[:,0], Y_sklearn[:,1], "bo", color=plt.cm.cool(np.array(DBPisa)/600).transpose())
"""

