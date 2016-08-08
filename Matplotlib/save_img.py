#!/usr/local/bin/python
# -*- coding:utf-8 -*-
'''
 @Author:      py.gooker
 @Email:       zhangshch0131@126.com
 @DateTime:    2016-05-06 18:24:26
 @Description: Description
'''

import matplotlib.pyplot as plt
import sys


def save1():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([1, 2, 3])
    fig.savefig('test.png')


def save2():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([1, 2, 3])

    fig.savefig(sys.stdout)


if __name__ == '__main__':
    save1()
    # save2()
