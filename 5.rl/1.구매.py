from cgitb import text
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

chrome.get("https://shopping.naver.com/home/p/index.naver")

# login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a#gnb_login_button")))
login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a#gnb_login_button")))
print(login_button.text)
login_button.click()

time.sleep(3)
chrome.close()