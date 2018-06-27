# coding:utf-8
import requests
import json
import re
from selenium import webdriver
import time
import csv


f = open('result.csv', 'w')
writer = csv.writer(f)
writer.writerow(['微信号', '公众号名称', '发布时间', '文章标题', '采集时间'])


with open('cookie.txt') as f:
    cookie = json.load(f)
    print(cookie)


response = requests.get('https://mp.weixin.qq.com/', cookies=cookie)
token = re.findall(r'token=(.*)', response.url)[0]

searchbi_params = {
    'action': 'search_biz',
    'ajax': '1',
    'begin': '0',
    'count': '5',
    'f': 'json',
    'lang':	'zh_CN',
    'query': 'gh_b76d6d056512',
    'random': '0.44021360219252215',
    'token': token
}

searchbi_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
searchbi_response = requests.get(searchbi_url, cookies=cookie, params=searchbi_params)

data = searchbi_response.json()
fake_id = data.get('list')[0].get('fakeid')

appmsg_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'
appmsg_params = {
    "token": token,
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "random": "0.7970007833411443",
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "",
    "fakeid": fake_id,
    "type": "9"
}

appmsg_response = requests.get(appmsg_url, params=appmsg_params, cookies=cookie)
app_msg_cnt = appmsg_response.json().get('app_msg_cnt') // 5 + 1

browser = webdriver.Chrome()
for i in range(app_msg_cnt):
    begin = i * 5
    appmsg_params = {
        "token": token,
        "lang": "zh_CN",
        "f": "json",
        "ajax": "1",
        "random": "0.7970007833411443",
        "action": "list_ex",
        "begin": '{}'.format(begin),
        "count": "5",
        "query": "",
        "fakeid": fake_id,
        "type": "9"
    }
    appmsg_response = requests.get(appmsg_url, params=appmsg_params, cookies=cookie)
    app_msg_list = appmsg_response.json().get('app_msg_list')
    for item in app_msg_list:
        a_id = item.get('aid')
        link = item.get('link')
        print(link)
        browser.get(link)
        time.sleep(2)
        publish_time = re.findall(r'<em id="publish_time".*?meta_text">(.*?)</em>', browser.page_source)[0]
        gongzhonghao = browser.find_element_by_id('js_name').text.strip()
        title = browser.find_element_by_id('activity-name').text.strip()
        crawl_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        writer.writerow([a_id, gongzhonghao, publish_time, title, crawl_time])

browser.close()
