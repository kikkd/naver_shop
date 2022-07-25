from sre_constants import CATEGORY
from unicodedata import category
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

chrome = webdriver.Chrome("./chromedriver.exe")
wait = WebDriverWait(chrome,10)
short_wait = WebDriverWait(chrome,3)

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

# cpu, 메인보드, 메모리, 그래픽카드, ssd, 케이스, 파워
# cpu 한번 클릭

Category = {
    "CPU" : "873",
    "메인보드" : "875",
    "메모리" : "874",
    "그래픽카드" : "876",
    "SSD" : "32617",
    "케이스" : "879",
    "파워" : "880",
}

Category_css = {
    c:"dd.category_"+Category[c]+" a" for c in Category
    # "CPU" : "dd.category_"+Category["메인보드"]+" a",
}
print(Category_css)

chrome.get("https://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16")

# find_visible("iframe#ifrmWish")
# chrome.switch_to.frame("ifrmWish") # 이전 프레임 사용 시절 스위치 방법

# CPU 카테고리 클릭
find_visible(Category_css["CPU"]).click()
# cpu = find_visible("dd.category_"+Category["메인보드"]+" a") # dd안에 있는 a를 선택
# cpu = find_visible("dd.category_" + Category["CPU"])
# find_visible("dd.category_873").click()
# cpu.click()
time.sleep(1)



time.sleep(3)
chrome.close()



