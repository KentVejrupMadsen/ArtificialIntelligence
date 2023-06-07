from elements import class_name__special_new_files__next_button, class_name__special_new_files__links
from selenium import webdriver

from selenium.webdriver.chrome.service import service

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
import json

counter = 0

driverOptions = ChromeOptions()
#driverOptions.add_argument("")

Driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=driverOptions)

wikicommons_url_new = "https://commons.wikimedia.org/wiki/Special:NewFiles"
continueTraversing = True

toSearch = []

found_urls = []


def entry(filename, url):
    return {"index": increment_of_counter(), "url": url, "filename": filename}


def gather_links():
    global Driver, found_urls
    found_elements = Driver.find_elements(By.CLASS_NAME, class_name__special_new_files__links())

    for e in found_elements:
        href = e.get_attribute("href")
        title = e.get_attribute("title")

        found_urls.append(entry(title, href))


def find_next():
    global Driver, toSearch

    try:
        e = Driver.find_element(By.CLASS_NAME, class_name__special_new_files__next_button())
        href = e.get_attribute("href")
        toSearch.append(href)

    except (Exception):
        print()


def get_latest_link():
    global toSearch
    c = toSearch[0]
    toSearch.pop(0)

    return c


def goto(link):
    global Driver

    Driver.get(link)
    Driver.implicitly_wait(30)


def increment_of_counter():
    global counter
    counter = counter + 1
    return counter


def truncate():
    global found_urls

    size = len(found_urls)

    if size >= 250:
        global counter

        for e in found_urls:
            result_output = json.dumps(
                e, indent=2
            )

            print(result_output)

        found_urls.clear()


def wait():
    time.sleep(1)


def main_process():
    global wikicommons_url_new, \
        continueTraversing, \
        toSearch

    toSearch.append(wikicommons_url_new)

    while continueTraversing:
        find_next()

        if len(toSearch) == 0:
            break

        current = get_latest_link()
        goto(current)
        wait()

        gather_links()

        truncate()


if __name__ == '__main__':
    main_process()