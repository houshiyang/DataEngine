# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:14:31 2021

@author: houshiyang
"""

import numpy as np
import xlrd

def read_excel():
    workBook = xlrd.open_workbook('grade.xlsx')
    allSheetNames = workBook.sheet_names()
    #print('All sheets names are: ', allSheetNames)
    sheet1Name = workBook.sheet_names()[0]
    #print('First sheet name is: ', sheet1Name)
    sheet1Content = workBook.sheet_by_name('Sheet1')
    #print('Sheet info: ', sheet1_content, sheet1_content.name, sheet1_content.nrows, sheet1_content.ncols)
    return sheet1Content

#语文、数学、英语成绩情况
chinese = read_excel().col_values(1)
del chinese[0]
chineseMean = np.mean(chinese)
chineseMax = max(chinese)
chineseMin = min(chinese)
chineseStd = np.std(chinese)
chineseVar = np.var(chinese)
print('语文成绩：', chineseMean, chineseMax, chineseMin, chineseStd, chineseVar)

math = read_excel().col_values(2)
del math[0]
mathMean = np.mean(math)
mathMax = max(math)
mathMin = min(math)
mathStd = np.std(math)
mathVar = np.var(math)
print('数学成绩：', mathMean, mathMax, mathMin, mathStd, mathVar)

english = read_excel().col_values(3)
del english[0]
englishMean = np.mean(english)
englishMax = max(english)
englishMin = min(english)
englishStd = np.std(english)
englishVar = np.var(english)
print("英语成绩：", englishMean, englishMax, englishMin, englishStd, englishVar)

#个人总分及排名
gradeSum = {}
zhangFei = read_excel().row_values(1)
del zhangFei[0]
gradeSum['zhangfei'] = sum(zhangFei)

guanYu = read_excel().row_values(2)
del guanYu[0]
gradeSum['guanyu'] = sum(guanYu)

liuBei = read_excel().row_values(3)
del liuBei[0]
gradeSum['liubei'] = sum(liuBei)

dianWei = read_excel().row_values(4)
del dianWei[0]
gradeSum['dianWei'] = sum(dianWei)

xuChu = read_excel().row_values(5)
del xuChu[0]
gradeSum['xuchu'] = sum(xuChu)
print(gradeSum)
print(sorted(gradeSum.values(), reverse = True))
print(gradeSum)













