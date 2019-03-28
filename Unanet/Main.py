from os import sys, path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import time
import project_expense_account
import standard_functions
import settings
from pynput.keyboard import Controller

# Main.py kicks off the script


# prompt User to choose direction of information, ie export or import
settings.URL = input("What is the URL? \nPaste from 'http://' until '/action'\n")
settings.username = input("Enter the username: ")
settings.password = input("Enter the password: ")
settings.direction = input("Would you like to Export or Import? ")

# initialize keyboard controller
settings.keyboard = Controller()

# initialize web browser used to retrieve / input information
standard_functions.initialize_browser()

# call the login function
standard_functions.login()

# determine which part of Unanet we are importing / exporting from
if settings.importType == "project_expense_account":
    # Kick off process
    project_expense_account.navigate()
else:
    "Choose a portion of the database to run this procedure on."

# exit out of web browser
time.sleep(1)
settings.driver.quit()
