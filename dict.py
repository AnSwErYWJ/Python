#!/usr/bin/env python
# coding=utf-8

# dict也是一个集合,查找速度快，占用内存多，key不能重复不能改变，无序

d = {
    'one':1,
    'two':2,
    'three':3
}

#长度
print (len(d))

#访问
if 'one' in d:
    print d['one']

print d.get('one') #key不存在返回None

#更新
d['four'] = 4
print d

d['one'] = 11 #key已经存在则替换原value
print d

#遍历
for key in d:
    print key+':',d[key]
