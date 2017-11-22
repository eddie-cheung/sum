#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.oschina.net/blog")

time.sleep(5)

for i in range(3):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage")
    time.sleep(3)

print browser.page_source
