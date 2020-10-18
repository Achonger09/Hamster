from selenium import webdriver
import time

class DownHtml(object):

    '''
    根据url 和buttom 下载网页源码
    '''
    def __init__(self, url , file_path, **kargs):
        '''
        初始化
        '''
        self.file_path = file_path
        self.browser = webdriver.Chrome()
        self.browser.get(url)

    def click_button(self, button_key):
        '''
        鼠标点击事件
        '''
        button = self.browser.find_element_by_css_selector('#su')
        button.click()

    def login(self, username, passwd):
        input = self.browser.find_element_by_css_selector('#login_field')
        input.send_keys(username)
        input = self.browser.find_element_by_css_selector('#password')
        input.send_keys(passwd+"\n")

    def download_html(self, url):
        '''
        return html source
        '''
        self.browser.get(url)
        html_source = self.browser.page_source.encode("gbk", "ignore")
        self.browser.close()
        with open(self.file_path, 'w') as f:
            f.write(str(html_source))
'''
url = 'https://github.com/login'
path = './web_source.html'
dh = DownHtml(url,path)
dh.login("xxxx","xxxx")
dh.download_html("https://github.com/Achonger09/gitbook/commits/master")
'''
