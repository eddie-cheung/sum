#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("https://weibo.com/")

time.sleep(5)
browser.find_element_by_name("username").send_keys("xhzhang44555@sina.com")
browser.find_element_by_name("password").send_keys("Zhangxuhui1991")
browser.find_element_by_xpath("//div[@class='info_list login_btn']/a[@node-type='submitBtn']").click()

print browser.page_source
