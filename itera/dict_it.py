#!/usr/bin/env python
# coding=utf-8

#迭代dict
#value
d = {'one':1,'two':2,'three':3}
print d.values() #将dict转换为包含value的list

for v in d.values():
    print v

print d.itervalues() #没转换，只是取出，节省内存
for v in d.itervalues():
    print v


#key and value
print d.items() #转换为包含tuple的list
for key,value in d.items():
    print key,':',value

print d.iteritems() #不断取出tuple，节省内存
for t in d.iteritems():
    print t
