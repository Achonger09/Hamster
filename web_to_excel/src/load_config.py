import configparser
import os

class LoadConfig(object):

    def __init__(self, path):
        '''
        读取配置文件信息
        '''
        config = configparser.ConfigParser()
        config.read(path)
        self.config = config

    def get_title_key(self, key, section):
        '''
        获取配置文件中key对应的value
        '''
        title = self.config.get(section, key)
        return title
    
    def get_all_title_key(self,section):
        '''
        获取配置文件中所有的key
        '''
        return self.config.options(section)

    def get_all_sections(self):
        '''
        获取配置文件中的sections
        '''
        return self.config.sections()

'''
path = './.config/config.ini'

lc = LoadConfig(path)
print(lc.get_title_key("title1"))

print(lc.get_all_title_key())
'''