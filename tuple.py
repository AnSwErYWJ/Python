#!/usr/bin/env python
# coding=utf-8

#tuple中文翻译为元组，和List类似，但是一旦建立不可修改

t = ('1','2','3')
print (t)
print (t[0])
print (t[-1])

#单元素
s = (1,) #不加，则会被认为时运算式
print (s)

#可变的
v = (1,2,[3,4])
print (v)
#tuple不变指的是元素指向不变
l = v[2]
l[0] = 5
l[1] = 6
print v
