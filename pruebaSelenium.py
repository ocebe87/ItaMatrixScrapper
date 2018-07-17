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
exitAirport = "BCN"
arriveAirport = "VLC"

driver = webdriver.Firefox()
driver.get(urlWeb)


def method_name():
    global elem, wait, airportCode, xpathSelector_, el
    elem = driver.find_element_by_xpath(CITY_PAIR_ORIG_)
    elem.clear()
    elem.send_keys(exitAirport)
    wait = WebDriverWait(driver, 10)
    airportCode = exitAirport
    xpathSelector_ = "//span[contains(text(),'(" + airportCode + ")')]"
    el = wait.until(EC.element_to_be_clickable((By.XPATH, xpathSelector_))).click()


method_name()

elem = driver.find_element_by_xpath(CITY_PAIR_DEST_)
elem.clear()
elem.send_keys(arriveAirport)
airportCode = arriveAirport
xpathSelector_ = "//span[contains(text(),'(" + airportCode + ")')]"
el = wait.until(EC.element_to_be_clickable((By.XPATH, xpathSelector_))).click()

elem = driver.find_element_by_xpath(CITY_PAIR_OUT_DATE_)
elem.clear()
elem.send_keys("08/03/2018")
elem.send_keys(Keys.INSERT)

elem = driver.find_element_by_xpath(PAIR_RET_DATE_)
elem.clear()
elem.send_keys("08/05/2018")
elem.send_keys(Keys.INSERT)

driver.find_element_by_xpath('//*[@id="searchButton-0"]').click()
