#!/usr/bin/env python
# coding=utf-8

# read file

# read([size]) no size for all
# readline([size]) one line
# readlines([size]) read all file,return every line of list.it's size is io.Default_buf_size(8192)

f = open('test.txt','r')

#print f.read()

#print f.readline()
#print f.readline(2)

#print f.readlines()

iter_f = iter(f) #revert to iter_f
lines = 0
for line in iter_f:
    lines += 1
    print line
print lines
