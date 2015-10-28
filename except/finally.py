#!/usr/bin/env python
# coding=utf-8

# finally主要用来清理
# 先执行finally再处理异常

try:
    f = open('1.txt')
    print int(f.read())
finally:
    print "close"
    f.close()
