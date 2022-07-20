from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip #파이썬에서 클립보드를 사용하게 해 주는 라이브러리


chrome = webdriver.Chrome("./chromedriver.exe")
wait = WebDriverWait(chrome,10)
short_wait = WebDriverWait(chrome,3)

id = " "
pw = " "

chrome.get("https://shopping.naver.com/home/p/index.naver")

def wait1(CSS_selector):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,CSS_selector)))

##### 로그인 #####
login_button = wait1("a#gnb_login_button").click()
input_id = wait1("input#id")
input_pw = wait1("input#pw")

# login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a#gnb_login_button"))).click()
# input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input#id")))
# input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input#pw")))

### pip install pyperclip ###
pyperclip.copy(id)
input_id.send_keys(Keys.CONTROL,"v")
pyperclip.copy(pw)
input_pw.send_keys(Keys.CONTROL,"v")
input_pw.send_keys("\n")

# input_id.send_keys("id")
# input_pw.send_keys("pw")
# input_pw.send_keys("\n")


wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a#gnb_logout_button")))
##### 로그인 #####

##### 검색 #####
search = wait1("input._searchInput_search_input_QXUFf")
search.send_keys("아이폰 케이스")
time.sleep(1)
search.send_keys("\n")
##### 검색 #####

##### 첫번째 상품 클릭 #####
wait1("a[class^=basicList_link__]").click()

time.sleep(2)
print(chrome.window_handles)
chrome.switch_to.window(chrome.window_handles[1])
# chrome.window_handles[0] # 네이버 쇼핑
# chrome.window_handles[1] # 네이버 쇼핑에서 클릭한 상세 페이지
print(chrome.title)

time.sleep(3)

# chrome.close() # tab 끄기
chrome.quit() # 브라우저 끄기


##### 스크롤 추가 #####
# 스크립트 이용하기, 자바 스크립트를 이용하여 스크롤을 내림
# 자바스크립트를 사용시키기 위해 execute_script()를 사용함
# for i in range(8):
#     chrome.execute_script("window.scrollBy(0, 100000)")
#     time.sleep(1)
# chrome.execute_script("window.scrollBy(0, document.body.scrollHeight)")
##### 스크롤 추가 #####

##### 검색 결과 크롤링 #####
# 광고 삭제 추가
# wait1("div[class^=basicList_info_area__]")
# items = chrome.find_elements(By.CSS_SELECTOR,"div[class^=basicList_info_area__]")

# for item in items:
#     try:
#         item.find_element(By.CSS_SELECTOR,"button[class^=ad_ad_stk]")
#         continue
#     except:
#         pass
#     print(item.find_element(By.CSS_SELECTOR,"a[class^=basicList_link__]").text)
##### 검색 결과 크롤링 #####










