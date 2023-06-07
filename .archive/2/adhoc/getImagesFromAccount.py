from selenium import webdriver

from selenium.webdriver.chrome.service import service

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

start = 'https://commons.wikimedia.org/w/index.php?title=Special:ListFiles&limit=250&user=Askeuhd'

url_to_traverse = start

continueTraversing = True

buffer = []
images_urls = []

current = None

driverOptions = ChromeOptions()
driverOptions.add_argument("--headless")

Driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=driverOptions)


def done():
    global images_urls

    for e in images_urls:
        print(e)


def main_process():
    global continueTraversing, buffer, Driver

    begin()

    while continueTraversing:
        if len(buffer) == 0:
            break
        next()
        has_next()

        retrieve_links()

        wait()

    done()


def retrieve_links():
    global Driver

    elements = Driver.find_elements(By.CLASS_NAME, "image")

    for e in elements:
        found_img_url(get_link(e))


def get_link(element):
    return element.get_attribute("href")


def begin():
    global url_to_traverse, buffer
    buffer.append(url_to_traverse)


def next():
    global Driver, buffer

    current = buffer[0]
    buffer.pop(0)

    Driver.get(current)
    Driver.implicitly_wait(30)


def has_next():
    global Driver

    element = Driver.find_element(By.CLASS_NAME, 'TablePager-button-next')

    if element.get_attribute('aria-disabled').__str__() == 'true':
        return False

    link = element.find_element(By.CLASS_NAME, 'oo-ui-buttonElement-button')
    buffer.append(link.get_attribute('href'))

    return True


def wait():
    time.sleep(1)


def found_img_url(url):
    global images_urls
    images_urls.append(url)


if __name__ == '__main__':
    main_process()