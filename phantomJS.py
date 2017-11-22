#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver

browser = webdriver.PhantomJS()
browser.get("https://item.taobao.com/item.htm?id=559046678520&ali_refid=a3_430582_1006:1102378156:N:iphone8:b3e7c4b8d9b034bc6df90cb0042c4ff3&ali_trackid=1_b3e7c4b8d9b034bc6df90cb0042c4ff3&spm=a230r.1.14.1#detail")

print browser.page_source
browser.quit()
