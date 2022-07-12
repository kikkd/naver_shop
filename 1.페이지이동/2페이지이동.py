from selenium import webdriver
import time

# chrome = webdriver.Chrome("./chromedriver.exe")
# time.sleep(3)
# chrome.close()

### 크롬 옵션 ###
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") 
# 여러개의 탭을 띄우면 각 탭마다 프로그램이 돌아감, sandbox는 각 탭마다 프로그램을 따로 돌리는 격리, no-sandbox는 이걸 사용하지 않음
#options.add_argument("headless") # 제어하는 크롬창을 띄우지 않음

chrome = webdriver.Chrome("./chromedriver.exe",options=options)
chrome.get("https://naver.com")
chrome.get("https://shopping.naver.com/home/p/index.naver")
chrome.back()
chrome.forward()

time.sleep(3)
chrome.close()
