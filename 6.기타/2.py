from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

options = webdriver.ChromeOptions()
options.headless = True

chrome = webdriver.Chrome("./chromedriver.exe",options=options)
wait = WebDriverWait(chrome,10)
short_wait = WebDriverWait(chrome,3)


##### 함수 #####
#=========================================================================================================================
def find_present(CSS):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,CSS)))

def finds_present(CSS):
    find_present(CSS)
    return chrome.find_elements(By.CSS_SELECTOR,CSS)

def find_visible(CSS):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,CSS)))

def finds_visible(CSS):
    find_visible(CSS)
    return chrome.find_elements(By.CSS_SELECTOR,CSS)
#=========================================================================================================================


##### 페이지 이동 #####
#=========================================================================================================================
# chrome.get("https://e-ks.kr/streamdocs/view/sd;streamdocsId=72059207571509686")
chrome.get("https://www.naver.com/")
#=========================================================================================================================

##### 검색 결과 스크린샷 #####
#=========================================================================================================================
chrome.set_window_size(20000,1000000)
# chrome.save_screenshot("./test1.png") # 크롬창 스크린샷

bodys = find_visible("body")
bodys.screenshot("./test2.png")

chrome.quit()