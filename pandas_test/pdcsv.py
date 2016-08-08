#!/user/bin python
# -*- coding:utf-8 -*- 
'''
 @Author:        py.gooker
 @DateTime:    2015-06-11 11:47:29
 @Description: pandas 读取文件信息 
'''

import csv
import pandas as pd

def csv1():
    with open("marks.csv") as f :
        for line in f :
            print line

def csv2():
    # print dir(csv)
    csv_reader = csv.reader(open('marks.csv'))
    for row in csv_reader :
        print row

def csv3():
    marks = pd.read_csv('marks.csv')
    print marks
    print dir(marks)
def csv4():
    marks = pd.read_table('marks.csv',sep=',')
    print dir(marks)
    print marks
    print marks.index
    print marks.columns
    print marks['name'][1]
    print marks.sort(columns='python')
    print marks[:1]
    print marks[1:3]
    print marks['physics']

def pds():
    print dir(pd)

def xls1():
    xls = pd.ExcelFile("marks.xlsx")
    # print dir(xls)
    print "xls sheet names :" , xls.sheet_names
    st1 = xls.parse("Sheet1")
    print st1
if __name__ == '__main__':
    # csv1()
    # csv2()
    # csv3()
    # csv4()
    # pds()
    xls1()

