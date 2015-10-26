#!/usr/bin/env python
# coding=utf-8

#对list切片，tuple也是一样的

#取前n个元素
#方法一
L = [1,2,3,4]
n = 3
r = []
for i in range(n):
    r.append(L[i])
print (r)

#方法二
print L[0:3] #0-3，不包括3
print L[:3] #第一个索引为0可以省略

# 其它用法
print L[:] #全部，从头到尾
print L[::2] #每两个元素取出一个

print L[:-2] #1 2

