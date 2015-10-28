#!/usr/bin/env python
# coding=utf-8

# with可以自动清理
# with就是上下文管理：包含__enter__()和__exit__()两个方法，并且支持
# with obj as var: var接受__enter__()返回值，__exit__()清理

#主要用于文件和进程互斥

with open('1.txt') as f:
    print ('open')
    print f.closed

print f.closed
