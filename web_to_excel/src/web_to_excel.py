import time
from load_config import LoadConfig
from match_data  import MatchDATA
from handle_excel import HandleExcel

def write_excel_with_re_data(section,func_name,**kargs):
    '''
    根据section,取key,value,匹配data,写入excel
    '''
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
html_path = './source/Commits · Achonger09_gitbook.html'
source_excel_path = './excel/source.xlsx'
timestr = time.strftime("%d-%H-%M-%S")
output_excel_path = './excel/result-%s.xlsx' % timestr
pipe_name = 'data1'

##初始化
ld = LoadConfig(config_path)
md = MatchDATA(html_path)
he = HandleExcel(source_excel_path)
sections = ld.get_all_sections()
print(sections)

## type1使用get_default_re_result匹配数据
section = sections[0]
func = 'get_default_re_result'
write_excel_with_re_data(section,func)

## type2使用get_custome_result匹配数据
section2 = sections[1]
func2 = 'get_custome_result'
write_excel_with_re_data(section2,func2,source_str='custome')

## 保存excel
he.save(output_excel_path)

