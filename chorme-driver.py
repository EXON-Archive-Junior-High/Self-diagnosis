from selenium import webdriver   # selenium 프레임 워크에서 webdriver 가져오기
import time

NAME = ""
SCHOOL = ""
BIRTH_DAY = ""

print("자가진단 시작")
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")
url = 'https://eduro.goe.go.kr/stv_cvd_co00_002.do'        # 접속할 웹 사이트 주소 (네이버)
driver = webdriver.Chrome('D:/chromedriver.exe')  # 크롬 드라이버로 크롬 켜기
driver.get(url)                 # 저장한 url 주소로 이


birth = driver.find_element_by_id('frnoRidno')
birth.clear()
birth.send_keys(BIRTH_DAY)


name = driver.find_element_by_id('pName')
name.clear()
name.send_keys(NAME)


schoolName = driver.find_element_by_id('schulNm')
schoolName.clear()
schoolName.send_keys(SCHOOL)


button = driver.find_element_by_id('btnConfirm')
button.click()
#학교정보 때문에 먹히는 현상으로 다시 한번
button.click()

time.sleep(1)
b1 = driver.find_element_by_id('rspns011')
b1.click()

b2 = driver.find_element_by_id('rspns02')
b2.click()

b3 = driver.find_element_by_id('rspns070')
b3.click()

b4 = driver.find_element_by_id('rspns080')
b4.click()

b5 = driver.find_element_by_id('rspns090')
b5.click()

button = driver.find_element_by_id('btnConfirm')
button.click()

print("완료")
time.sleep(5)


