#!/usr/bin/env python
# coding=utf-8

import os
import os.path
import ConfigParser

class student_info(object):
    
    #初始化
    def __init__(self,recordfile):
        self.logfile = recordfile
        self.cfg = ConfigParser.ConfigParser()

    #读取文件
    def cfg_load(self):
        self.cfg.read(self.logfile)
    
    #读取文件内容
    def cfg_dump(self):
        se_list = self.cfg.sections()
        print "====================>"
        for se in se_list:
            print se
            print self.cfg.items(se)
        print "====================>"

    #删除key
    def delete_item(self,section,key):
        self.cfg.remove_option(section,key)

    #删除section
    def delete_section(self,sescion):
        self.cfg.remove_section(section)

    #添加section
    def add_section(self,section):
        self.cfg.add_section(section)

    #添加或修改
    def set_item(self,section,key,value):
        self.cfg.set(section,key,value)

    #保存文件
    def save(self):
        fp = open('self.ini','w')
        self.cfg.write(fp)
        fp.close()

if __name__ == '__main__':
    info = student_info('test.ini')
    info.cfg_load()
    info.cfg_dump()
    info.set_item('userinfo','pwd','123456')
    info.cfg_dump()
    info.add_section('login')
    info.set_item('login','2015-0511','20')
    info.cfg_dump()
    info.save()
    
