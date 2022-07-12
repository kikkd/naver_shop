from selenium import webdriver
import time

chrome = webdriver.Chrome("./chromedriver.exe")
time.sleep(3)
chrome.close()

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
time.sleep(3)
browser.close()

