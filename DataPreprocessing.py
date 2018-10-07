#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 12:22:32 2018

@author: shuvamoymondal
"""

""""Data
Country,Age,Salary,Purchased
France,44,72000,No
Spain,27,48000,Yes
Germany,30,54000,No
Spain,38,61000,No
Germany,40,,Yes
France,35,58000,Yes
Spain,,52000,No
France,48,79000,Yes
Germany,50,83000,No
France,37,67000,Yes
""""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer,LabelEncoder,OneHotEncoder,StandardScaler, Normalizer
from sklearn.cross_validation import train_test_split



data=pd.read_csv('/Users/shuvamoymondal/Desktop/Machine Learning A-Z Template Folder/Part 1 - Data Preprocessing/Data.csv')

""" X- Independent variable and take all lines and all fileds except last one"""
X=data.iloc[:, :-1].values
""" y- Dependent variable and take all lines and  last fields purchase"""
y=data.iloc[:,3].values


##How to take care NaN value with Imputer
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer=imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])

## Encoding Categorical data as 2 clumns has categorical values for country and purchase
## Need to use LabelEncoder for encoding the value and then if we have more categorial value, we can 
## classify with 0 and 1 value by using OneHotEncoder inorderwise
labelEncoder_X=LabelEncoder()
X[:,0]=labelEncoder_X.fit_transform(X[:,0])
oneHotEncoder=OneHotEncoder(categorical_features=[0])
X=oneHotEncoder.fit_transform(X).toarray()

##Same for dependent variable Y 
labelEncoder_y=LabelEncoder()
y=labelEncoder_y.fit_transform(y)

##Split the data for training and test data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

## Feature Scaling: Sometime there is huge difference between fetures while squaring betwwen min and max value(example: Salary and age here )
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)  ## we do not need fit_transform as its fit for X_train above
