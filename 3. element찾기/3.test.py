from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import warnings

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 셀레니움 로그 무시
warnings.filterwarnings("ignore", category=DeprecationWarning) # Deprecated warning 무시 

browser = webdriver.Chrome(options = chrome_options)
browser.get('https://www.naver.com')
browser.implicitly_wait(10) #로딩이 끝날동안 10초 기다린다

browser.find_element(By.CSS_SELECTOR, 'a.nav.shop').click() #쇼핑메뉴 클릭
time.sleep(2)

#검색창 클릭
search = browser.find_element(By.CSS_SELECTOR, 'input._searchInput_search_input_QXUFf')
search.click()

#검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)