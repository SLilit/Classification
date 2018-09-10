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

d
