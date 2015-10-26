#!/usr/bin/env python
# coding=utf-8

#索引迭代
#将每个元素变成一个tuple，（0，1）（1，2）。。。
L = [1,2,3,4]
for index,name in enumerate(L):
    print index,'-',name
