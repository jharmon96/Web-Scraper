import time
import project_expense_account
import standard_functions
import settings
from selenium import webdriver
from pynput.keyboard import Controller

# Main.py kicks off the script


# prompt User to choose direction of information, ie export or import
settings.direction = input("Would you like to export or import? ")

# initialize keyboard controller
settings.keyboard = Controller()

# initialize web browser used to retrieve / input information
settings.driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

# call the login function
standard_functions.login()

# determine which part of Unanet we are importing / exporting from
if settings.import_type == "project_expense_account":
    project_expense_account.navigate()

# exit out of web browser
time.sleep(1)
settings.driver.quit()

