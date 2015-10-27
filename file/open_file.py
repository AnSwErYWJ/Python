#!/usr/bin/env python
# coding=utf-8

# open file

f = open('test.txt','a+')
print type(f)

c = f.read()
print c

f.close()

