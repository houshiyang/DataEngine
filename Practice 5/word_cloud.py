# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 20:39:33 2021

@author: houshiyang
"""

#利用Python进行词云展示
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
import pandas as pd


#数据加载
data = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)
print('data', data)
print('data-shape', data.shape)

#将数据存放到transaction, shape[0]为行数，shape[1]为列数
transactions = []
#存储计数字典
item_count = {}


for i in range(data.shape[0]):
    temp = []
    for j in range(data.shape[1]):
        #取出数据，清洗
        item = str(data.values[i, j])
        if item != 'nan':
            temp.append(item)
            #计数
            if item not in item_count:
                item_count[item] = 1
            else:
                item_count[item] += 1
    transactions.append(temp)
print('transactions', transactions)


#去掉比较常用的虚词停用词
def remove_stop_words(f):
    #预设要去掉的词列表
    stop_words = ['and', 'for', 'as', 'the']
    for stop_word in stop_words:
        #将停用词替换为空
        f = f.replace(stop_word, '')
    return f
    
    
def create_word_cloud(f):
    f = remove_stop_words(f)
    # Q:word_tokenize作用是啥？？？ 
    cut_text = word_tokenize(f)
    cut_text = " ".join(cut_text)
    wc = WordCloud(
        max_words = 200, #调节词个数
        width = 2000,
        height = 1200
        )
    wordcloud = wc.generate(cut_text)
    wordcloud.to_file("word_cloud.jpg")
    
    
#生成词云
all_word = ' '.join('%s' %item for item in transactions)
print('all_word', all_word)
create_word_cloud(all_word)
    
    
    
    
    
    
    
    