# coding:utf-8
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def taobao_search_ipad():
    """
    打开淘宝， 搜索ipad
    """
    browser = webdriver.Chrome()
    url = 'https://www.taobao.com'
    browser.get(url)
    input = browser.find_element(By.ID, 'q')
    input.send_keys('ipad')
    btn_search = browser.find_element(By.CLASS_NAME, 'btn-search')
    btn_search.click()
    browser.close()


def drag_and_drop():
    """
    http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
    拖拽， 释放
    """
    browser = webdriver.Chrome()
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to_frame('iframeResult')
    target = browser.find_element(By.ID, 'droppable')
    source = browser.find_element(By.ID, 'draggable')
    action = ActionChains(browser)
    action.drag_and_drop(source, target)
    action.perform()
    browser.close()


def url_back_and_forward():
    """输入网址， 前进， 后退"""
    browser = webdriver.Chrome()
    browser.get('http://www.taobao.com')
    browser.get('http://www.baidu.com')
    browser.get('http://www.zhihu.com')
    browser.back()
    time.sleep(1)
    browser.forward()


def new_window():
    """打开新的选项卡，进行不同操作"""
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    # 执行js创建新的选项卡
    browser.execute_script('window.open()')
    handles = browser.window_handles
    # 切换到第二个选项卡，在第二个选项卡上进行操作
    browser.switch_to_window(handles[1])
    browser.get('https://www.zhihu.com')
    time.sleep(1)
    browser.execute_script('window.open()')
    # 切换到第一个选项卡，在第一个选项卡上进行操作
    browser.switch_to_window(handles[0])
    browser.get('https://www.baidu.com')
    time.sleep(1)


if __name__ == '__main__':
    # taobao_search_ipad()
    # drag_and_drop()
    # url_back_and_forward()
    new_window()
