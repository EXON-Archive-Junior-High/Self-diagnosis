from selenium import webdriver
import time


CHROME_DRIVER = "" #ex) D:/chromedriver.exe
NAME = ""
SCHOOL = ""
BIRTH_DAY = "" #ex) 071022


f = open("Time.txt", 'r')
t = f.read()

if (t != time.strftime('%d', time.localtime(time.time()))):
    f.close()
    f = open("Time.txt", 'w')
    f.write(time.strftime('%d', time.localtime(time.time())))
    f.close()

    print("자가진단 시작")

    url = 'https://eduro.goe.go.kr/stv_cvd_co00_002.do'
    driver = webdriver.Chrome(CHROME_DRIVER)
    driver.get(url)

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
else:
    print("이미 자가진단을 하셨습니다.")
    f.close()


