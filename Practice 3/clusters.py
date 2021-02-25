# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 09:20:32 2021

@author: houshiyang
"""


#使用K-means进行聚类
from sklearn.cluster import KMeans
#用于预处理，本例应用LabelEncoder和无量纲处理
from sklearn import preprocessing
import pandas as pd
import numpy as np

#数据输入
data = pd.read_csv('car_data.csv', encoding = 'gbk')
train_x = data[["地区", "人均GDP", "城镇人口比重", "交通工具消费价格指数", "百户拥有汽车量"]]


#LabelEncoder将非数值标签转为数值标签
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
#???? Q1：fit_transform后编码与原表格index不一致
#比如：['北京', '天津', '河北', ...] 对应变为[3, 6, 16, ...]
train_x['地区'] = le.fit_transform(train_x['地区'])
memo_train_x = le.inverse_transform(train_x['地区'])
print('train_x', train_x)
print('memo_train_x', memo_train_x)


#无量纲化到[0, 1]空间
min_max_scaler = preprocessing.MinMaxScaler()
#???? Q2：fit_transform后，LableEncoder产生的编码也被无量纲化了？
train_x = min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_csv('temp.csv', index = False)
print('train_x_standradized', train_x)


#使用KMeans聚类
#创建分类器对象
kmeans = KMeans(n_clusters = 4)
#用训练器数据拟合分类器模型
kmeans.fit(train_x)
#对训练器数据进行预测
predict_y = kmeans.predict(train_x)
#合并聚类结果，插入原表格
#在column方向将结果进行连接
result = pd.concat((data, pd.DataFrame(predict_y)), axis = 1)
result.rename({0:u'聚类结果'}, axis = 1, inplace = True)
print('result', result)


#结果导出
result.to_csv("car_clusters.csv", index = False)
result.to_excel("car_clusters.xlsx", index = False)



#手肘法：统计不同簇数值的误差平方和
import matplotlib.pyplot as plt
sse = []
for k in range(1, 11):
    #kmeans算法
    kmeans = KMeans(n_clusters = k)
    kmeans.fit(train_x)
    #计算簇内误差平方和
    sse.append(kmeans.inertia_)
    
x = range(1, 11)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()




#使用层次聚类
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt
#linkage四种连接方法：ward(默认), complete, average, single
model = AgglomerativeClustering(linkage = 'ward', n_clusters = 4)
y = model.fit_predict(train_x)
#????Q3：y是按什么顺序排列的？
print('y', y)

linkage_matrix = ward(train_x)
#dendrogram：专门用来描述层次聚类算法的结果
dendrogram(linkage_matrix)
plt.show()









