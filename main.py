#-*- coding: utf-8 -*-
from selenium import webdriver
import time


CHROME_DRIVER = "chromedriver.exe"
NAME = ""
SCHOOL = ""
BIRTH_DAY = "" #ex) 071022

setting = open("setting.txt", 'r', encoding='UTF8')
t = setting.read()

a = t.split(',')
NAME = a[0]
SCHOOL = a[1]
BIRTH_DAY = a[2]

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/83.0.4103.116 "
        "Safari/537.36"
        )
options.add_argument("disable-gpu")

f = open("Time.txt", 'r')
t = f.read()

if (t != time.strftime('%d', time.localtime(time.time()))):
    f.close()
    f = open("Time.txt", 'w')
    f.write(time.strftime('%d', time.localtime(time.time())))
    f.close()

    print("자가진단 시작")

    url = 'https://eduro.goe.go.kr/stv_cvd_co00_002.do'
    driver = webdriver.Chrome(CHROME_DRIVER, options=options)
    driver.get(url)

    birth = driver.find_element_by_id('frnoRidno')
    birth.clear()
    birth.send_keys(BIRTH_DAY)
    print("생년월일 입력")

    name = driver.find_element_by_id('pName')
    name.clear()
    name.send_keys(NAME)
    print("성명 입력")

    schoolName = driver.find_element_by_id('schulNm')
    schoolName.clear()
    schoolName.send_keys(SCHOOL)
    print("학교이름 입력")

    button = driver.find_element_by_id('btnConfirm')
    button.click()
    #학교정보 때문에 먹히는 현상으로 다시 한번

    button.click()
    print("")

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
else:
    print("이미 자가진단을 하셨습니다.")
    f.close()


