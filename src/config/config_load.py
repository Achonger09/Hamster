#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import os

class ConfigLoad(object):
    '''
    读取config.ini文件内容，并返回
    '''
    def __init__(self):
        root_path = os.path.dirname(os.path.abspath(__file__))
        print(root_path)
        ##目前路径固定，暂不修改
        config_path = os.path.join(root_path,"..\\..\\config\\config.ini")
        print(config_path)
        self.conf= configparser.ConfigParser()
        self.conf.read(config_path)

    def get(self,*args):
        return self.conf.get(*args)

    def options(self,session):
        return self.conf.items(session)

