from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

options = webdriver.ChromeOptions()
options.headless = True # headless로 화면이 켜지지 않게 한다. 설정한 options을 webdriver에 적용해야만 실제로 적용됨

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
chrome.get("https://www.naver.com/")
find_visible("input#query").send_keys("패스트캠퍼스\n")
#=========================================================================================================================

##### 검색 결과 스크린샷 #####
#=========================================================================================================================
e = find_visible("li[data-cr-rank='1']")
# chrome.execute_script("document.querySelector(\"li[data-cr-rank=\"1\"]\").setAttribute(\"style\",\"border:10px solid red\")")

chrome.execute_script("""document.querySelector('li[data-cr-rank="1"]').setAttribute("style","border:10px solid red")""")
print(e.text)
e.screenshot("./test1.png") # 해당 엘리먼트를 스크린샷

chrome.set_window_size(1000,10000)
chrome.save_screenshot("./test2.png") # 크롬창을 스크린샷

bodys = find_visible("body") # 전체 body를 css selector로 잡아 전체 화면을 스크린샷함
bodys.screenshot("./test3.png")
#=========================================================================================================================


chrome.quit()