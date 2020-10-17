import time
from load_config import LoadConfig
from match_data  import MatchDATA
from handle_excel import HandleExcel

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

keystr_list = ld.get_all_title_key()
## 遍历config中的key
for keystr in keystr_list:
    ## 取config中key对应的value用于 匹配date 
    value = ld.get_title_key(keystr)
    ## 取value 在html中匹配的data
    data = md.get_re_result(value)
    ## 数据写入excel
    he.write_by_name(pipe_name, keystr,data)

## 保存excel
he.save(output_excel_path)
