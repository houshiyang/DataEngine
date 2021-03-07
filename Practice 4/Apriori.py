# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:15:13 2021

@author: houshiyang
"""

import pandas as pd

#打印所有数据，不用省略
pd.set_option('max_column', None)
#加载数据，注意：数据源第一行无表头，需要设置header
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
print('dataset', dataset)
print('dataset_shape', dataset.shape)

#存放所有记录
transactions = []
#数据遍历
for i in range(0, dataset.shape[0]):
    #记录一行transaction
    temp = []
    for j in range(0, dataset.shape[1]):
        if str(dataset.values[i, j]) != 'nan':
            temp.append(dataset.values[i, j])
    #print(temp)
    transactions.append(temp)
    
from efficient_apriori import apriori
itemsets, rules = apriori(transactions, min_support = 0.02, min_confidence = 0.3)
print('频繁项集itemsets：', itemsets)
print('关联规则rules：', rules)
        








