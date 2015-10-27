#!/usr/bin/env python
# coding=utf-8

#底层模块
import os

fd = os.open('os.txt',os.O_CREAT|os.O_RDWR)

print os.access('os.txt',os.F_OK)
print os.access('os.txt',os.R_OK)
print os.access('os.txt',os.W_OK)
print os.access('os.txt',os.X_OK)

print os.listdir('./')

#os.rename(old,new)
#os.remove(filename)

n = os.write(fd,'nihao')
print n

l = os.lseek(fd,0,os.SEEK_SET)
print l

print os.read(fd,5)

os.close(fd)

