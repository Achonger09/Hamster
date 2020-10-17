import re
import os

class MatchDATA(object):

    def __init__(self,str_path):
        '''
        根据正则表达式匹配出满足条件的数据
        注: 正则表达式请根据实际情况改写
            可实现多个正则表达式
        str_path 匹配文件的路径
        '''
        self.re_format = ".*aria-label=\"%s\".*href=\"(.*)\".*"
        with open(str_path, encoding='utf-8') as f:
            context = f.read()
        self.cotext = context

    def get_format(self):
        '''
        返回正则表达式模板
        '''
        return self.re_format
    
    def get_re_result(self, key_str, source_str=None):
        '''
        返回满足条件的data
        '''
        if not source_str:
            source_str = self.cotext
        format = self.re_format % key_str
        print('find %s in str' % format)
        res = re.search(format, source_str)
        print('find result :%s' % res.group(1))
        return res.group(1)

'''
md = MatchDATA()
print(md.get_format())
with open('./source/Commits · Achonger09_gitbook.html',encoding='utf-8') as f:
    context = f.read()

print(md.get_re_result('etcd',context))
'''