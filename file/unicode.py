#!/usr/bin/env python
# coding=utf-8

import codecs

f = codecs.open('test.txt','a+','utf-8')

print f.encoding

f.write(u'你好')

f.close()
