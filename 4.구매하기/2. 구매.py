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

id = ""
pw = ""

chrome.get("https://shopping.naver.com/home/p/index.naver")

def wait1(CSS_selector):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,CSS_selector)))

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

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a#gnb_btn_login")))

time.sleep(3)

chrome.close()