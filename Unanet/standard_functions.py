import csv
import os
from pynput.keyboard import Key
import time
import settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path

home = str(Path.home())

# starts google chrome in either headless (export) or standard (import) mode.

def initialize_browser():
    if settings.direction == "Export":
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")
        settings.driver = webdriver.Chrome(options=options, executable_path=home + r"\drivers\chromedriver.exe")

    # If importing, open browser. This is because the import feature uses the 'enter' key to input data
    elif settings.direction == "Import":
        settings.driver = webdriver.Chrome(executable_path=home + r"\drivers\chromedriver.exe")


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

    if input_value is not "":
        settings.driver.find_element_by_xpath('//*[@id="ac-input"]').send_keys(input_value)
        time.sleep(1)
        settings.keyboard.press(Key.enter)
        settings.keyboard.release(Key.enter)

    settings.driver.find_element_by_xpath('//*[@id="button_save"]').click()


# exports information from Unanet

def fileExport(input_file):
    fnames = ["expense_type", "expense_type_key", "project_type", "project_type_key", "account"]

    with open(os.path.join(os.environ["HOMEPATH"], "Desktop",settings.file), 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=fnames, lineterminator='\n')
        dict_writer.writeheader()
        dict_writer.writerows(input_file)
