# coding:utf-8
from selenium import webdriver
import time
from pprint import pprint
import json


browser = webdriver.Chrome()
browser.get('https://mp.weixin.qq.com/')
account_input = browser.find_element_by_name('account')
pwd_input = browser.find_element_by_name('password')
cb_remeber = browser.find_element_by_class_name('icon_checkbox')
btn_login = browser.find_element_by_class_name('btn_login')


cookie = {}

account_input.clear()
account_input.send_keys('1228381225@qq.com')
pwd_input.clear()
pwd_input.send_keys('wx122838')
cb_remeber.click()
btn_login.click()

time.sleep(15)

cookies = browser.get_cookies()
for item in cookies:
    cookie[item.get('name')] = item.get('value')

pprint(cookies)

with open('cookie.txt', 'w') as f:
    json.dump(cookie, f)

time.sleep(5)
browser.close()

