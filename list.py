#!/usr/bin/env python
# coding=utf-8

# list是有序集合，其中可以包含不同类型的元素

#构建
L =['one',1,'two',2,'three',3]

#访问
print (L)
print (L[0])
print (L[-1]) #最后一个元素，-2为倒数第二个，以此类推

#添加
L.append('four') #追加到末尾
print (L)

L.insert(0,'zero') #可以指定位置
print (L)

#删除
L.pop() #删除队尾元素并返回
print (L)

L.pop(0) #删除指定位置
print (L)

#替换
L[0] = 'zero'
L[-1] = 'four'
print (L)
