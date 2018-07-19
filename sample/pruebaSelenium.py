from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from sample.Flight import Flight

DIV_ = "div"
CLASS_ = "class"
FLIGHT_BOX_ = "IR6M2QD-u-j"
TIME_DIVS_ = "IR6M2QD-u-f"
AIRLINE_DIV_ = {CLASS_: "IR6M2QD-u-b"}
BOX_ORIG_ = '//*[@id="cityPair-orig-0"]'
BOX_DEST_ = '//*[@id="cityPair-dest-0"]'
OUT_DATE_ = '//*[@id="cityPair-outDate-0"]'
RET_DATE_ = '//*[@id="cityPair-retDate-0"]'
SEARCH_BUTTON_ = '//*[@id="searchButton-0"]'
LOADING_MESSAGE_ = '/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[6]/div[5]/div/div/a'

urlWeb = "http://matrix.itasoftware.com/"
driver = webdriver.Firefox()
driver.get(urlWeb)
wait = WebDriverWait(driver, 100)


def fill_suggestion_box(selector, airport):
    global elem, wait, airportCode, xpathSelector_, el
    elem = driver.find_element_by_xpath(selector)
    elem.clear()
    elem.send_keys(airport)
    el = wait.until(EC.element_to_be_clickable((By.XPATH, ("//span[contains(text(),'(" + airport + ")')]")))).click()


def fill_date_box(selector, data):
    elem = driver.find_element_by_xpath(selector)
    elem.clear()
    elem.send_keys(data)
    elem.send_keys(Keys.INSERT)


def search_page():
    fill_search_fields()
    driver.find_element_by_xpath(SEARCH_BUTTON_).click()


def fill_search_fields():
    fill_suggestion_box(BOX_ORIG_, "BCN")
    fill_suggestion_box(BOX_DEST_, "VLC")
    fill_date_box(OUT_DATE_, "08/03/2018")
    fill_date_box(RET_DATE_, "08/05/2018")


def result_page():
    wait.until_not(EC.element_to_be_clickable(
        (By.XPATH, LOADING_MESSAGE_)))
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    flights = []
    for f in soup.findAll(DIV_, {CLASS_: FLIGHT_BOX_}):
        airLine = f.find(DIV_, AIRLINE_DIV_).string
        departureGo = f.findAll(DIV_, {CLASS_: TIME_DIVS_})[0].string
        arriveGo = f.findAll(DIV_, {CLASS_: TIME_DIVS_})[1].string
        departureCome = f.findAll(DIV_, {CLASS_: TIME_DIVS_})[2].string
        arriveCome = f.findAll(DIV_, {CLASS_: TIME_DIVS_})[3].string

        flights.append(Flight(airLine, departureGo, arriveGo, departureCome, arriveCome))
    flights.count()


search_page()

result_page()
