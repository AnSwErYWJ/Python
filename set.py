#!/usr/bin/env python
# coding=utf-8

# set的元素无重复，无序的，和dict很像；set有一系列元素，这和list很像

# 创建
s = set(['one','two','three'])
print (s)

# set会自动去除重复元素

# set无法访问，只能判断是否存在

# set和dict的区别时不存储value，查找速度很快。并且，key不可变，元素无序。

# 遍历
for num in s:
    print (num)

# 更新
s.add('four') #已经存在则不会添加
print s
if 'one' in s:
    s.remove('one')
    print s

# 应用
x = 'Mon'
weekdays = set(['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
if x in weekdays:
    print ("OK")
else:
    print ("Error")
