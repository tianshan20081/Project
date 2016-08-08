#!/user/bin python
# -*- coding:utf-8 -*- 
'''
 @Author:        py.gooker
 @DateTime:    2015-06-11 10:31:35
 @Description: pandas 基础语法练习 
'''

from pandas import Series,DataFrame
import pandas as pd
def series1():
    s = Series([100,200,'PYTHON','PANDAS','DJANGO'])
    print s
    print s.index
    print s.values
    print s[2]
def series2():
    s = Series([100,'python','java'],index=['name',2,'j'])
    print s.index
    print s.values
    print s['name']
    print 's[1]' ,s[1]
    print 's[2]' ,s[2]
    # print 's[age]' ,s['age']
    print s
    print 'update value'
    s['j'] = 'javascript'
    print s

def sd():
    sd = {'python':8080,'c++':8100,'java':9000}
    s = Series(sd)
    print s
def sd2():
    sd = {'python':8000,'java':9000}
    s = Series(sd,index=['python','java','c#'])
    print s
    print pd.isnull(s)
    print s.isnull()
def s3():
    s = Series([3,4,6,9],index=['a','b','c','f'])
    s2 =  Series([10,50,100,200],index=['a','b','c','f'])
    print s 
    print s[s > 5]
    print s * 5
    print s + s2

    ss1 = ['ja','py']
    ss2 = ['va','thon']
    s3 = Series(ss1)
    s4 = Series(ss2)
    print s3 + s4
    s5 = Series(ss1,index=['j','y'])
    s6 = Series(ss2,index = ['j','y'])
    print s5 + s6
    s7 = Series(ss1,index=['j','y'])
    s8 = Series(ss2,index = ['y','j'])
    print s7 + s8

def df1():
    data = {'name':['yahoo','google','baidu'],\
    'marks':[200,400,100],'price':[6,4,1]}
    f1 = DataFrame(data)
    print f1
    f2 = DataFrame(data,columns=['name','price','marks'])
    print f2
    f3 = DataFrame(data,columns=['name','price','marks']\
        ,index=['a','c','b'])
    print f3
    f4 = DataFrame(data,\
        columns=['name','price','marks','debt']\
        ,index=['a','c','b'])
    print f4

    data2 = {"lang":{'firstline':'python','secondline':'java'},\
    'price':{'firstline':8000}}
    f5 = DataFrame(data2)
    print f5
    f6 = DataFrame(data2,index=['firstline','secondline','thirdline'])
    print f6

    print f3.columns
    print f3['name']

    f4['debt'] = 89.2
    print f4

    sdebt = Series([1.3,6.7],index=['a','b'])
    f3['debt'] = sdebt
    print f3
    f3['price']['c'] = 10
    print f3
    
if __name__ == '__main__':
    # series1()
    # series2()
    # sd()
    # sd2()
    # s3()
    df1()


