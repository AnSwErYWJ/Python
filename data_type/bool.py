#!/usr/bin/env python
# coding=utf-8

print (100 < 99) #False
print (True and False) #False
print (True or False) #True
print (not False) #True

#空字符串，None，0为False
print ('' or False)
print (None or False)
print (0 or False)

a = 10 
print type(a)
a = '10' 
print type(a)
a = False 
print type(a)
