import time
from load_config import LoadConfig
from match_data  import MatchDATA
from handle_excel import HandleExcel
from down_html import DownHtml

def write_excel_with_re_data(section,**kargs):
    '''
    根据section,取key,value,匹配data,写入excel
    '''
    func_name = ld.get_title_key(section, "Function")
    keystr_list = ld.get_all_title_key(section)
    ## 遍历config中Type1的key
    for keystr in keystr_list:
        ## 取config中key对应的value用于 匹配date 
        value = ld.get_title_key(keystr,section)
        ## 取value 在html中匹配的data
        func = 'md.' + func_name
        #data = md.get_re_result(value)
        data = eval(func)(value,**kargs)
        ## 数据写入excel
        he.write_by_name(pipe_name, keystr,data)

config_path = './.config/config.ini'
timestr = time.strftime("%d-%H-%M-%S")
output_excel_path = './excel/result-%s.xlsx' % timestr
pipe_name = 'data1'
username = "xxxx"
passwd = "xxxx"
url = 'https://github.com/login'
html_source = "https://github.com/Achonger09/gitbook/commits/master"
html_path = './source/Commits · Achonger09_gitbook.html'
source_excel_path = './excel/source.xlsx'

## 下载html source文件
dh = DownHtml(url,html_path)
dh.login(username,passwd)
dh.download_html(html_source)

##初始化
ld = LoadConfig(config_path)
md = MatchDATA(html_path)
he = HandleExcel(source_excel_path)

sections = ld.get_all_sections()
sections.remove("Function")
print(sections)
## type1使用get_default_re_result匹配数据
section = sections[0]
write_excel_with_re_data(section)

## type2使用get_custome_result匹配数据
section2 = sections[1]
write_excel_with_re_data(section2,source_str='custome')

## 保存excel
he.save(output_excel_path)
