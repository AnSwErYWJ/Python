#!/usr/bin/env python
# coding=utf-8

# write

# write(str)
# writelines(sequence of strings)

f = open('test.txt','a+')

#f.write('\nmy write')
f.writelines('\n123456\n')
f.writelines(['1','2','3'])
f.writelines(('1','2','3'))

#f.flush()
#f.close()

# write cache,need close or flush to use

