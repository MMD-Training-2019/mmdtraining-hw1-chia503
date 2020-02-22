# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 00:14:20 2019

@author: User
"""

import sys
import numpy as np
import csv

mean = np.load('mean.npy')     
std = np.load('std.npy')
w_1 = np.load('weight_1_best.npy')  
w_2 = np.load('weight_2_best.npy')                              
test_old_data = np.genfromtxt(sys.argv[1], delimiter=',')   
test_data = test_old_data[:, 2: ]
Nan = np.isnan(test_data)
test_data[Nan] = 0

test_x = np.empty(shape = (240, 18 * 9),dtype = float)

for i in range(240):
    test_x[i,:] = test_data[18 * i : 18 * (i+1),:].reshape(1,-1) 

mean = np.mean(test_x, axis = 0) 
std = np.std(test_x, axis = 0)
for i in range(test_x.shape[0]):        
    for j in range(test_x.shape[1]):
        if not std[j] == 0 :
            test_x[i][j] = (test_x[i][j]- mean[j]) / std[j]


test_x = np.concatenate((np.ones(shape = (test_x.shape[0],1)),test_x),axis = 1).astype(float)
test_x_2degree = test_x**2
answer = test_x.dot(w_1) + test_x_2degree.dot(w_2)

f = open(sys.argv[1],"w")
w = csv.writer(f)
title = ['id','value']
w.writerow(title) 
for i in range(240):
    content = ['id_'+str(i),answer[i][0]]
    w.writerow(content) 