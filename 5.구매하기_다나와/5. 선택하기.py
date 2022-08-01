from itertools import count
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

def choose_one(text, opsions):
    print("----------------")
    print(text)
    for i in range(len(opsions)):
        print(f"{i+1}. {opsions[i]}")
    chooses = input("=> ")
    return int(chooses) - 1

def parse_product():
    # left_frame()
    time.sleep(1)
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

def go_to_category(category_name):
    # 카테고리 클릭
    find_visible(Category_css[category_name]).click()
    # 옵션 전체 보기
    find_visible("div[class=search_option_title] button[class=search_option_all]").click()
    time.sleep(1)
    # 전체 옵션들의 상세 전체보기 클릭
    more_options = finds_visible(f"div[class=search_option_list] div[class=search_option_item] div[class=search_cate_contents] button[class=btn_item_more]")
    for i in more_options:
        try:
            i.click()
        except:
            pass
        # more_options[i].click()
    time.sleep(1)

def opsion(i):
    time.sleep(1)
    str(i)
    options = finds_visible(f"div[class=search_option_list] div[class=search_option_item]:nth-child({i}) label[class=item_checkbox] span[class=item_text]")
    # more_options = finds_visible(f"div[class=search_option_list] div[class=search_option_item] div[class=search_cate_contents] button[class=btn_item_more]")
    # more_options[0].click()
    time.sleep(1)
    return options

def choose_maker(text):
    # left_frame()
    options = opsion(1)
    i = choose_one(text, [x.text for x in options])
    # print(len(options))
    print(options[i].text)
    options[i].click()
    return i

def get_opsion(title):
    # left_frame()
    return finds_visible(f"select[title='{title}'] option:not[vlaue='']")

# cpu, 메인보드, 메모리, 그래픽카드, ssd, 케이스, 파워
# cpu 한번 클릭

# print(Category_css)

chrome.get("https://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16")

###
# right_frame():
# CPU 카테고리 클릭
# find_visible(Category_css["CPU"]).click()
# cpu = find_visible("dd.category_"+Category["메인보드"]+" a") # dd안에 있는 a를 선택
# cpu = find_visible("dd.category_" + Category["CPU"])
# find_visible("dd.category_873").click()
# cpu.click()
# time.sleep(1)
go_to_category("CPU")

# 옵션 전체보기 클릭
# find_visible("button[onmousedown^=gtagSend]").click()

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
maker_idx = choose_maker("CPU 제조사를 골라주세요.")

# options = opsion(1)
# # options[10].click()

# i = choose_one("CPU 제조사를 골라주세요", [x.text for x in options])
# print(len(options))
# print(options[i].text)
# options[i].click()

# for i in range(len(options)):
#     print(str(i+1)+". "+options[i].text)
    # options[i]

# for o in options:
#     print(o.text)

#### CPU 종류 선택
is_intel = False
is_amd = False
if maker_idx == 0:
    is_intel = True
    options = opsion(2)
    i = choose_one("인텔 CPU 종류 선택", [x.text for x in options])
    print(options[i].text)
    options[i].click()
elif maker_idx == 1:
    is_amd = True
    options = opsion(3)
    i = choose_one("AMD CPU 종류 선택", [x.text for x in options])
    print(options[i].text)
    options[i].click()

### CPU 목록 선택하기
# 상품명
# div[class=scroll_box] tr[class^=productList_] p.subject a
# 가격
# div.scroll_box tr[class^=productList_] span.prod_price
# time.sleep(1)
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
# for cpu in cpus:
#     print(cpu)   

##### 메인보드 #####
go_to_category("메인보드")

choose_maker("메인보드 제조사를 골라 주세요.")
# options = opsion(1)
# i = choose_one("메인보드 제조사를 골라주세요", [x.text for x in options])
# print(options[i].text)
# options[i].click()
print("----------------")
print("제품 분류 선택")
options = opsion(2)
if is_intel:
    options[0].click()
    print("=> 인텔 선택 완료")
elif is_amd:
    options[1].click()
    print("=> amd 선택 완료")

## 메인보드 목록 가져오기
mainboards = parse_product()

##### 메모리 #####
go_to_category("메모리")

choose_maker("메모리 제조사를 골라 주세요")

print("----------------")
print("사용 장치 선택")
options = opsion(2)
options[0].click()
print("=> 데스크탑용 선택 완료")

print("----------------")
print("제품 분류 선택")
options = opsion(3)
options[1].click()
print("=> DDR4 선택 완료")

print("----------------")
print("메모리 용량 선택")
options = opsion(4)
i = choose_one("메모리 용량을 선택 해 주세요", [x.text for x in options])
print(options[i].text)
options[i].click()

mamoris = parse_product()

##### 그래픽 카드 #####

# 그래픽 카드
go_to_category("그래픽카드")

choose_maker("그래픽카드 제조사를 골라 주세요")

print("----------------")
print("칩셋 제조사 선택")
options = opsion(2)
if is_intel:
    options[0].click()
    print("=> 인텔 호환 NVIDIA 선택 완료")
elif is_amd:
    options[1].click()
    print("=> amd 호환 AMD 선택 완료")

print("----------------")
if is_intel:
    print("NVIDIA 칩셋 선택")
    options = opsion(5)
    chip_set = "NVIDIA"
elif is_amd:
    print("AMD 칩셋 선택")
    options = opsion(6)
    chip_set = "AMD"
i = choose_one(f"{chip_set} 칩셋을 선택 해 주세요", [x.text for x in options])
print(options[i].text)
options[i].click()

graphics = parse_product()

##### SSD #####
# 그래픽 카드
go_to_category("SSD")

choose_maker("SSD 제조사를 골라 주세요")

print("----------------")
print("SSD 용량 선택")
options = opsion(5)
i = choose_one("용량을 선택 해 주세요", [x.text for x in options])
print(options[i].text)
options[i].click()

ssds = parse_product()

##### 케이스 #####
# 케이스
go_to_category("케이스")

choose_maker("케이스 제조사를 골라 주세요")

print("----------------")
print("제품 분류 선택")
options = opsion(2)
i = choose_one("제품 분류 선택 해 주세요", [x.text for x in options])
print(options[i].text)
options[i].click()

print("----------------")
print("지원 파워 규격 선택")
options = opsion(4)
i = choose_one("지원 파워 규격을 선택 해 주세요", [x.text for x in options])
print(options[i].text)
options[i].click()

cases = parse_product()

# cpus mainboards mamoris graphics ssds cases
time.sleep(3)
chrome.close()



