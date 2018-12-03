from selenium import webdriver
from scrapy.selector import Selector

# 操作chrome浏览器
driver = webdriver.Chrome()
driver.get('http://report.bbtu.com/')
print(driver.page_source)
driver.quit()
