#!/usr/bin/env python
# coding=utf-8

import sys

print type(sys.stdin) #This is file
print sys.stdin.fileno()
print sys.stdout.mode
print ('\n')
# print = sys.stdout.write()


import sys
if __name__ == '__main__':
    print len(sys.argv)
    for arg in sys.argv:
        print arg
