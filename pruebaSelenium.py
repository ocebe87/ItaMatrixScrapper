from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

CITY_PAIR_ORIG_ = '//*[@id="cityPair-orig-0"]'
CITY_PAIR_DEST_ = '//*[@id="cityPair-dest-0"]'
CITY_PAIR_OUT_DATE_ = '//*[@id="cityPair-outDate-0"]'
PAIR_RET_DATE_ = '//*[@id="cityPair-retDate-0"]'

urlWeb = "http://matrix.itasoftware.com/"
driver = webdriver.Firefox()
driver.get(urlWeb)


def fieldSugestionBox(selector, airport):
    global elem, wait, airportCode, xpathSelector_, el
    elem = driver.find_element_by_xpath(selector)
    elem.clear()
    elem.send_keys(airport)
    wait = WebDriverWait(driver, 10)
    xpathSelector_ = "//span[contains(text(),'(" + airport + ")')]"
    el = wait.until(EC.element_to_be_clickable((By.XPATH, xpathSelector_))).click()


def method(selector, data):
    elem = driver.find_element_by_xpath(selector)
    elem.clear()
    elem.send_keys(data)
    elem.send_keys(Keys.INSERT)


fieldSugestionBox(CITY_PAIR_ORIG_, "BCN")
fieldSugestionBox(CITY_PAIR_DEST_, "VLC")

method(CITY_PAIR_OUT_DATE_, "08/03/2018")
method(PAIR_RET_DATE_, "08/05/2018")

driver.find_element_by_xpath('//*[@id="searchButton-0"]').click()
