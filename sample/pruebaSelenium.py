from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# from Flight import Flight
from sample.Flight import Flight

BOX_ORIG_ = '//*[@id="cityPair-orig-0"]'
BOX_DEST_ = '//*[@id="cityPair-dest-0"]'
OUT_DATE_ = '//*[@id="cityPair-outDate-0"]'
RET_DATE_ = '//*[@id="cityPair-retDate-0"]'
SEARCH_BUTTON_ = '//*[@id="searchButton-0"]'

urlWeb = "http://matrix.itasoftware.com/"
driver = webdriver.Firefox()
driver.get(urlWeb)
wait = WebDriverWait(driver, 100)


def field_suggestion_box(selector, airport):
    global elem, wait, airportCode, xpathSelector_, el
    elem = driver.find_element_by_xpath(selector)
    elem.clear()
    elem.send_keys(airport)
    el = wait.until(EC.element_to_be_clickable((By.XPATH, ("//span[contains(text(),'(" + airport + ")')]")))).click()


def field_date_box(selector, data):
    elem = driver.find_element_by_xpath(selector)
    elem.clear()
    elem.send_keys(data)
    elem.send_keys(Keys.INSERT)


field_suggestion_box(BOX_ORIG_, "BCN")
field_suggestion_box(BOX_DEST_, "VLC")

field_date_box(OUT_DATE_, "08/03/2018")
field_date_box(RET_DATE_, "08/05/2018")

driver.find_element_by_xpath(SEARCH_BUTTON_).click()

h3 = wait.until_not(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[6]/div[5]/div/div/a')))

soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.prettify())

for f in soup.findAll("div", {"class": "IR6M2QD-u-j"}):
    airLine = f.find("div", {"class": "IR6M2QD-u-b"}).text
    airLine = f.findAll("div", {"class": "IR6M2QD-u-f"}).text
    f.get('a')

    flight = Flight(airLine, '', '')
