#!/usr/bin/env python
# coding=utf-8

try:
    f = open('1.txt')
    line = f.read(2)
    num = int(line)
    print "read num=%d" % num
except IOError,e:
    print "catch IOError:",e
except ValueError,e:
    print "catch ValueError:",e

else:
    print "no error"

