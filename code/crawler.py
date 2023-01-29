from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

process_save_dir = r"D:\Workspace\codespace\spaces\python\data"

option = webdriver.ChromeOptions()

option.add_argument("user-data-dir=" + r"D:\tmp\automated chrome")
#option.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)

keepRunning = True
counter = 0
next_element = None

buffer = []
history = []
blacklist = []


def isBlacklisted(href):
    global blacklist

    for e in blacklist:
        if e == href:
            return True

    return False

def now():
    global buffer, \
           history

    r = buffer[0]
    buffer.pop(0)
    history.append(r)

    return r


def click_download_original():
    global driver

    try:
        downloadOriginal = driver.find_element(By.CLASS_NAME, "Original")
        downloadOriginal.click()

    except:
        print("Error: Download Original")


def download():
    global driver

    try:
        downloadButton = driver.find_element(By.CLASS_NAME, "download")
        downloadButton.click()

        click_download_original()
    except:
        print("Error")


def increment():
    global counter
    counter = counter + 1


def reset():
    global counter
    counter = 0


def get_counter():
    global counter
    return counter


def still_running():
    global driver

    try:
        current = driver.current_url
        print("here: " + current)

        return True
    except:
        return False


def exist_next_element_and_setup_next_page():
    global driver

    try:
        next = driver.find_element(By.CLASS_NAME, "navigate-next")
        href = next.get_attribute("href")

        appendToBuffer(href)

        return True
    except:
        print("error")

    return False


def operation():
    global keepRunning, \
           driver

    url = now()
    driver.get(url)

    sleep(3.5)

    increment()

    if not isBlacklisted(url):
        download()

    if get_counter() % 5 == 0:
        reset()
        snapshot()
        update()

    if not still_running():
        keepRunning = False

    if not exist_next_element_and_setup_next_page():
        print("Stopped: No more images in the ALBUM")


def snapshot():
    global driver, process_save_dir

    tFile = time.time_ns()
    driver.save_screenshot(process_save_dir + '\\' + str(int(tFile)) + ".png")


def appendToBuffer(href):
    global buffer
    buffer.append(href)


def bufferIsEmpty():
    global buffer
    if len(buffer) == 0:
        return True
    return False


def setup():
    global blacklist

def collision(href):
    return collision_buffer(href) or collision_history(href)


def collision_history(href):
    global history

    for e in history:
        if e == href:
            return True

    return False


def collision_buffer(href):
    global buffer

    for e in buffer:
        if e == href:
            return True

    return False


def update():
    global history
    print("sorting history:")
    history.sort()


def main():
    global driver, \
           keepRunning

    setup()

    driver.maximize_window()

    while keepRunning:
        operation()

        if bufferIsEmpty():
            break

    driver.quit()


def find_license_all_rights():
    global driver

    try:
        licenseArea = driver.find_element(By.CLASS_NAME, "photo-license-url")
        el = licenseArea.find_element(By.TAG_NAME, "span")

        if str(el.text).lower() == r'some rights reserved':
            return True
    except:
        print('Error Occured in finding license.')

    return False


def sleep(value):
    global driver
    driver.implicitly_wait(value)


if __name__ == '__main__':
    main()
