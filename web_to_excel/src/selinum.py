from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
time.sleep(2)
input = browser.find_element_by_css_selector('#kw')
input.send_keys("yes man")
button = browser.find_element_by_css_selector('#su')
button.click()
time.sleep(2)

websource = browser.page_source.encode("gbk", "ignore")
with open('web.html','w') as f:
    f.write(str(websource))

browser.close()