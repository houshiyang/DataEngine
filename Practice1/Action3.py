# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:02:34 2021

@author: houshiyang
"""

import pandas as pd

#数据加载
df = pd.read_csv('./car_complain.csv')
print(df)

#数据清洗函数
def f(x):
    x = x.replace('一汽-大众', '一汽大众')
    return x

#数据预处理
#get_dummies把problem中的问题全部展成列，用0/1表示是否存在
df = df.drop('problem', axis = 1).join(df.problem.str.get_dummies(','))

#按品牌统计
df['brand'] = df['brand'].apply(f)
resultBrand = df.groupby(['brand'])['id'].agg(['count'])
print(resultBrand)

#按problem拆分统计
tags = df.columns[7:]
resultTags = df.groupby(['brand'])[tags].agg(['sum'])
print(resultTags)

#按投诉总数排序
resultTags = resultBrand.merge(resultTags, left_index = True, right_index = True, how = 'left')
resultTags.reset_index(inplace = True)
print(resultTags)
#resultTags.to_csv('./result.csv')
#按照count从大到小进行排序
resultTags = resultTags.sort_values('count', ascending = False)
#按照problem指定问题进行查询、排序
query = ('A12', 'sum')
resultTags.sort_values(query, ascending = False)












