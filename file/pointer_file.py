#!/usr/bin/env python
# coding=utf-8

import os #for whence

# seek(offset[,whence]): move file pointer
# tell():return current file position

f = open('test.txt','r+')

print f.read(3)
print f.tell()

f.seek(0,os.SEEK_SET)

print f.tell()
print f.read()

f.seek(0,os.SEEK_END)
print f.tell()
print f.read()

f.seek(-5,os.SEEK_CUR)
print f.tell()
print f.read()
print f.tell()

f.close()
