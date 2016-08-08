#!/user/bin python
# -*- coding:utf-8 -*-
'''
 @Author:      py.gooker
 @Email:       zhangshch0131@126.com
 @DateTime:    2016-03-16 12:56:32
 @Description: pandas test

 Pandas有两种主要的数据结构：
 Series和Dataframe，前者是一维的，后者是多维的（表格型）。
'''
import pandas  as pd

# 一、Series
# Series由一组数据和对应的索引组成，
def series_test():
    lx = [7,6,5,4]
    a = pd.Series(lx)
    print(a)
# 我们也可以用index=来指定索引：
    b = pd.Series(lx,index=['mozi','gooker','python','java'])
    print(b)
    print(b['mozi'])
    print('mozi' in b)

# 实际上，字典也确实可以直接变身成为Series！
# 比如下面的字典a，储存了每个地区的平均工资，将其变为Series：
    a = {'bj':7000,'sh':6500,'sz':6000,'xa':5500}
    print(a)
    print(pd.Series(a))
    print(pd.Series(a,index=['bj','xa']))


# 1. 数据结构
# DataFrame是一个表格型的数据结构。
def dataframe_test():
    pop={'city':['Chongqin', 'Shanghai', 'Beijing', 'Chengdu', 'Tianjin', 'Guangzhou', 'Baoding', 'Harbin', 'Suzhou', 'Shenzhen'],
            'pop':[2884.6, 2301.9, 1961.2, 1404.8, 1293.8, 1270.1, 1119.4, 1063.6, 1046.6, 1035.8]}
    print(pop)
    pop_df = pd.DataFrame(pop)
    print(pop_df)
# 也可以用columns=[]来指定某列：
    pop_df = pd.DataFrame(pop,columns=['city'])
    print(pop_df)

# 2. 基本操作
# 认识几个基本操作，加深一下印象。
# （1）改变索引名
# 刚刚的城市人口数据，我们有10个城市，索引是0~9，我们不想用这么单调的数字来做索引，
# 想用每个城市的简称来表示，和Series一样，可以用index=来指定索引：
# （因为Python自带的shell中，结果的显示没有ipython notebook美观，
# 所以下面的例子我用ipython notebook的结果来展示）
    pop_df = pd.DataFrame(pop, index=['Yu', 'Hu', 'Jing', 'Rong', 'Jin', 'Sui', 'Bao', 'Ha', 'Su', 'Shen'])
    print(pop_df)

# （2）增加一列
# 如何给DataFrame增加一列？还是以刚刚城市人口的数据pop_df为例，
# 我们来增加一列，给每个城市打上“China”的标记：
    pop_df['country'] = 'China'
    print(pop_df)

    province = pd.Series(['GuangDong','JiangSu'],index=['Sui','Su'])
    pop_df['province'] = province
    print(pop_df)
# 这里我get了两点：
# 1. 可以用Series来按照索引的匹配来增加一列；
# 2. 缺失的地方会用NaN来表示。

# 3）排序
# 作为统计师，排序是常见的，我想到的以后可能用到的至少有这几种：
# 人为给定顺序；
# 按照索引来自动排序：升序、降序；
# 按照某一变量来自动排序；

# 人为给定顺序：
# 用reindex函数，可以人为的给定顺序，想让谁在前面谁就在前面。

    pop_df2 = pop_df.reindex(['Bao','Ha','Hu','Jin','Jing','Rong','Shen','Su','Sui','Yu'])
    print(pop_df2)
    pop_df2 = pop_df.reindex(['Shan','Bao','Ha','Hu','Jin','Jing','Rong','Shen','Su','Sui','Yu'])
    print(pop_df2)

# 按照索引自动排序：
# 可以用 .sort_index() 来让数据按照索引自动排序。
# 在上例中，我们多了一个索引为“Chu”的空数据，并且在Bao的前面，
# 我们再用sort_index()让它按照字母顺序自动重排一下。
    print(pop_df2.sort_index())
# 这是默认的升序排列，也可以降序，只要指定ascending=False就可以：
    print(pop_df2.sort_index(ascending=False))

# 按照变量自动排序：
# 我们可以用  .sort_values( by = '' ) 来指定某一个变量来排序：
    print(pop_df.sort_values(by='pop'))
    print(pop_df.sort_values(by='pop',ascending=False))

# （4）删除一列
# 前面学的是改变索引名、增加一列、各种排序，
# 好像少掉了什么——如何删掉一列和一行...
# 用 .drop() 就可以删掉指定的索引行，比如我们想删掉pop_df中，
# 人口大于2000（万）的城市，也就是重庆和上海，对于的索引（也就是简称）为：Yu和Hu
    print(pop_df.drop(['Yu','Hu']))

# 那么删掉一列呢？
# 也是用 .drop()  ，指定一下要删的列变量，并且加一句 axis=1 。
    print(pop_df2.drop(['province'],axis=1))

if __name__ == '__main__':
    # series_test()
    dataframe_test()
