# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:26:17 2017

@author: iryna
"""

import pandas as pd
import os
os.getcwd()
os.chdir('/Users/iryna/dataOECD') 
LifeExpOrig=pd.read_csv("LifeExpectancy_HEALTH_STAT_23012017161027877.csv", sep=",",index_col="Country", usecols=["Variable","Country","Year","Value"])
LifeExpT=LifeExpOrig[LifeExpOrig["Variable"]=="Total population at birth"]
LifeExpT.head(3)
LifeExpT2000=LifeExpT[LifeExpT["Year"]==2000]
LifeExpT2000.head(3)
LifeExp=LifeExpT2000["Value"]

#LifeExp.shape
#LifeExp.index
LifeExp.loc["China"]=LifeExp.loc["China (People's Republic of)"]


PisaMa=pd.read_csv("average_maths.csv", sep=";", index_col=0,  usecols=[0,1])
PisaMa.index=PisaMa.index.str.strip()
PisaMa
PisaMa.loc["China"]=PisaMa.loc["Shanghai-China"]

PisaRe=pd.read_csv("average_reading_litteracy.csv", sep=";", index_col=0)
PisaRe.index=PisaRe.index.str.strip()
PisaRe.loc["China"]=PisaRe.loc["Shanghai-China"]

PisaPS=pd.read_csv("problem_solving.csv", sep=",", index_col=0)
PisaPS.index=PisaPS.index.str.strip()
PisaPS.loc["China"]=PisaPS.loc["Shanghai-China"]


PisaLifeExp=pd.concat([PisaMa,PisaRe,PisaPS,LifeExp], axis=1)#join='inner'
PisaLifeExp.columns=["PisaMaths","PisaReading","PisaProblemSolving","LifeExpectancyTotalPopAtBirthYear2000"]


PisaLifeExp.to_csv("PisaLifeExp.csv")

#AddingFinancing aborted for now: difficult to compare, missing data
EduFinanceOrig=pd.read_csv("EducationFinancing2013_EAG_FIN_RATIO_CATEGORY_22012017191457765.csv", index_col=1 )
#EduFinance.columns
EduFinance1=EduFinanceOrig.loc[:,['Level of education', 'Expenditure type', 'COUNTERPART_SECTOR','Year','Value']]
#EduFinance2=EduFinance1[EduFinance1['Level of education']==]



#https://www.stat.auckland.ac.nz/~ihaka/787/lectures-trellis.pdf


pd.read_csv("ours/OECD_v1.csv", index_col=0)
