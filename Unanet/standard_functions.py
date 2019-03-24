import time
import settings

from pynput.keyboard import Key, Controller


# logs into the browser with credentials provided in settings.py

def login():
    settings.driver.get(settings.URL + "/home")

    id_box = settings.driver.find_element_by_name('username')
    id_box.send_keys(settings.username)

    pass_box = settings.driver.find_element_by_name('password')
    pass_box.send_keys(settings.password)

    login_button = settings.driver.find_element_by_name('button_ok')
    login_button.click()


# imports information from file defined in settings.py

def fileImport(input_value):
    settings.driver.find_element_by_xpath('//*[@id="ac-input"]').clear()
    settings.driver.find_element_by_xpath('//*[@id="ac-input"]').send_keys(input_value)
    time.sleep(1)
    settings.keyboard.press(Key.enter)
    settings.keyboard.release(Key.enter)
    settings.driver.find_element_by_xpath('//*[@id="button_save"]').click()


# exports information from Unanet

def fileExport():
    input_value = str(settings.driver.find_element_by_xpath('//*[@id="ac-input"]').get_attribute("value"))
    print(input_value)
