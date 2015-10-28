#!/usr/bin/env python
# coding=utf-8

# 异常为运行时错误
#常见错误：
#NameError : a 
#SyntaxError : if True
#IOError : f=open('1.txt')
#ZeroDivisionError : 10/0
#ValueError : a=int('dd')

a = 0
try:
    a
except NameError,e:
    print 'catch error:',e

print "error over"
