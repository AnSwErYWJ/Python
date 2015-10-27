#!/usr/bin/env python
# coding=utf-8

import ConfigParser #配置文件库

cfg = ConfigParser.ConfigParser()

print cfg.read('test.ini')

print cfg.sections()

for se in cfg.sections():
    print se
    print cfg.items(se)

cfg.set('userinfo','pwd','123456')#更改

for se in cfg.sections():
    print se
    print cfg.items(se)

cfg.set('userinfo','email','ywj1993@yeah.net')#添加
cfg.remove_option('userinfo','email')#删除

