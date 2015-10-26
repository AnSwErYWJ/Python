#!/usr/bin/env python
# coding=utf-8

import math

# 函数没有return则返回None

def square_sum(L):
    sum = 0
    for x in L:
        sum += x * x
    return sum

print square_sum([1,2,3,4,5])

# 返回多值其实就是返回一个tuple
# 计算一元二次方程的两个解

def count(a,b,c):
    x = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    y = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x,y

print count(2,3,0)

x,y = count(2,3,0)
print x,y
