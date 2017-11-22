#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
#from scrapy.selector import selector
import time

browser = webdriver.Chrome()
#browser.get("https://detail.tmall.com/item.htm?spm=a230r.1.14.1.3a19ba983HpK0M&id=552919553653&cm_id=140105335569ed55e27b&abbucket=15&sku_properties=10004:827902415;5919063:6536025")
browser.get("https://www.zhihu.com/#signin")

browser.find_element_by_xpath("//div[@class='qrcode-signin-cut-button']/span[@class='signin-switch-password']").click()
#browser.find_element_by_name("account").send_keys("echochang0@gmail.com")
browser.find_element_by_xpath("//div[@class='view view-signin']/form[@method='POST']/div[@class='group-inputs']/div[@class='account input-wrapper']/input[@name='account']").send_keys("account")
browser.find_element_by_xpath("//div[@class='view view-signin']/form[@method='POST']/div[@class='group-inputs']/div[@class='verification input-wrapper']/input[@name='password']").send_keys("password")
time.sleep(10)
browser.find_element_by_xpath("//div[@class='view view-signin']/form/div[@class='button-wrapper command']/button[@class='sign-button submit']").click()

print browser.page_source
