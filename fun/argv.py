#!/usr/bin/env python
# coding=utf-8

#默认参数

# int()第二个参数为转换进制，默认为十进制

def power(x , n = 2):
    s = 1
    while n > 0:
        s *= x
        n -= 1
    return s

print power(2)
print power(2,3)

#可变参数
#被封装成tuple

def average(*args):
    sum = 0.0
    if len(args)==0:
        return sum
    for i in args:
        sum += i
    return sum/len(args)

print average()
print average(1,2,2,3,4)
