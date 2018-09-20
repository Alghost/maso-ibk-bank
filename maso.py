import time, datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

opts = webdriver.ChromeOptions()
# need it to be changed to yours
opts.add_argument("user-data-dir=/Users/taehwalee/Library/Application Support/Google/Chrome")
driver = webdriver.Chrome('./chromedriver', chrome_options=opts)

try:
    driver.get('https://kiup.ibk.co.kr/uib/jsp/guest/qcs/qcs10/qcs1010/PQCS101000_i.jsp')
    time.sleep(3)

    elem = driver.find_element_by_xpath('//*[@id="in_cus_acn"]')
    elem.send_keys('') # in_cus_acn
    
    elem = driver.find_element_by_xpath('//*[@id="acnt_pwd"]')
    ac = ActionChains(driver)
    ac.move_to_element(elem)
    ac.click()
    ac.send_keys('') # acnt_pwd
    ac.perform()

    elem = driver.find_element_by_xpath('//*[@id="rnno"]')
    ac.reset_actions()
    ac.move_to_element(elem)
    ac.click()
    ac.send_keys('') # rnno
    ac.perform()

    elem = driver.find_element_by_link_text('조회')
    elem.click()

    time.sleep(5)

    elem = driver.find_element_by_tag_name('canvas')
    source = elem.get_attribute('innerHTML')
    soup = BeautifulSoup(source, 'html.parser')
    rows = soup.find_all('tr')

    results = list()
    for row in rows:
        data = row.find_all('span')
        if data:
            results.append(tuple(x.get_text() for x in data))

    print('\n'.join([str(x) for x in results]))
    input()
except Exception as e:
    print(e)
finally:
    driver.quit()

