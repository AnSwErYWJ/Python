#!/usr/bin/env python
# coding=utf-8

print (abs(-10))
print (cmp(1,2))
print (int('123'))
print (int(123.123))
print (str(123))
print (str(1.23))

L = []
x = 1
while x <= 100:
    L.append(x*x)
    x += 1

print (sum(L))
