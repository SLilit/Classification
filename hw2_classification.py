from __future__ import division
import numpy as np
import pandas as pd
import sys
import math

data = pd.read_excel('C:/Users/DENVER/edX/ML/d.xlsx', sheetname = 0)
data1 = pd.read_excel('C:/Users/DENVER/edX/ML/t.xlsx', sheetname = 0)
X_train = np.array(data.iloc[:, :5])
y_train = np.array(data.iloc[:, -1:])
X_test = np.array(data1.iloc[:, :])
#print('train: ', X_train[:4])
#print('test: ', y_train[:4])
#print('test: ', X_test[:4])

def pluginClassifier(X_train, y_train, X_test):
    
  # this function returns the required output
    outputs = np.zeros(shape = (len(X_test),4))
    means = np.zeros(shape=(4,len(X_train[0])))
    covariences = np.array([[[0.]*5]*5]*4) 
    prior = np.zeros(shape = (4,1))
    count = np.zeros(shape = (5,1))
    cov_det = np.zeros(shape = (4,1))
