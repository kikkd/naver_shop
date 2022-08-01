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

### 페이지 iframe 스위치 함수
def right_frame():
    chrome.switch_to.parent_frame() # 부모 프레임으로 이동
    find_visible("iframe#ifrmWish")
    chrome.switch_to.frame("ifrmWish") # 이전 프레임 사용 시절 스위치 방법

def left_frame():
    chrome.switch_to.parent_frame() # 부모 프레임으로 이동
    find_visible("iframe#ifrmProduct")
    chrome.switch_to.frame("ifrmProduct")

def opsion(i):
    str(i)
    options = finds_visible(f"div[class=search_option_list] div[class=search_option_item]:nth-child({i}) label[class=item_checkbox] span[class=item_text]")
    more_options = finds_visible("div[class=search_option_list] div[class=search_option_item] div[class=search_cate_contents] button[class=btn_item_more]")
    more_options[0].click()
    return options

def choose_one(text, opsions):
    print("----------------")
    print(text)
    for i in range(len(opsions)):
        print(f"{i+1}. {opsions[i]}")
    chooses = input("=> ")
    return int(chooses) - 1

def parse_product():
    # left_frame()
    products = []
    for p in finds_visible("div[class=scroll_box] tr[class^=productList_]"):
        name = p.find_element(By.CSS_SELECTOR,"p.subject a").text
        try:
            price = p.find_element(By.CSS_SELECTOR,"span.prod_price").text
        except:
            # price = "판매준비"
            continue
        products.append((name, price))
    return products

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

###
# right_frame():
# CPU 카테고리 클릭
find_visible(Category_css["CPU"]).click()
# cpu = find_visible("dd.category_"+Category["메인보드"]+" a") # dd안에 있는 a를 선택
# cpu = find_visible("dd.category_" + Category["CPU"])
# find_visible("dd.category_873").click()
# cpu.click()
time.sleep(1)

# 옵션 전체보기 클릭
find_visible("button[onmousedown^=gtagSend]").click()

'''
###### 강의 코드 ######
## CPU 제조사 불러오기
left_frame()
options = finds_visible("select[name=srchMaker] option:not([value=''])")
i = choose_one("CPU 제조사를 골라 주세요.", [x.text for x in options])
options[i].click()

## CPU 종류 불러오기
title = ""
if i == 0:
    title = "인텔 CPU 종류 선택"
elif i == 1:
    title = "AMD CPU 종류 선택"
options = finds_visible(f"slect[title='{title}'] option:not([value=''])")
i = choose_one("종류를 선택 해 주세요")
'''



# CPU 제조사 불러오기
###
# left_frame()

### CPU 선택
options = opsion(1)
# options[10].click()

i = choose_one("CPU 제조사를 골라주세요", [x.text for x in options])
print(len(options))
print(options[i].text)
options[i].click()

# for i in range(len(options)):
#     print(str(i+1)+". "+options[i].text)
    # options[i]

# for o in options:
#     print(o.text)

#### CPU 종류 선택

if i == 0:
    options = opsion(2)
    i = choose_one("인텔 CPU 종류 선택", [x.text for x in options])
    print(options[i].text)
    options[i].click()
elif i == 1:
    options = opsion(3)
    i = choose_one("AMD CPU 종류 선택", [x.text for x in options])
    print(options[i].text)
    options[i].click()

### CPU 목록 선택하기
# 상품명
# div[class=scroll_box] tr[class^=productList_] p.subject a
# 가격
# div.scroll_box tr[class^=productList_] span.prod_price
time.sleep(1)
# products = finds_visible("div[class=scroll_box] tr[class^=productList_]")
# cpus = []
# for p in products:
#     name = p.find_element(By.CSS_SELECTOR,"p.subject a").text
#     try:
#         price = p.find_element(By.CSS_SELECTOR,"span.prod_price").text
#     except:
#         # price = "판매준비"
#         continue
#     cpus.append((name, price))

cpus = parse_product()
for cpu in cpus:
    print(cpu)   
    
time.sleep(3)
chrome.close()



