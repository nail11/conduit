
# Testing the main page's buttons and other element's existence and accessibility
#...................................................................................

# environment

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
#from random import randint
import pytest
#import requests
import time


options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "http://localhost:1667/#/"

# general settings

driver.get(url)

    # elements
butts = driver.find_elements_by_xpath('//*[@id="app"]/nav/div/ul/li/a')
home_butt = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[1]')

    # variables, data

butt_names = ("Home", "Sign in", "Sign up")
def main_butts_activate(button):
    button.click()
    time.sleep(1)

# function

def button_test(butts):
    for i, button in enumerate(butts):
        button = butts[i]
        butt_name = butt_names[i]
        main_butts_activate(button)
        assert driver.current_url == button.get_attribute("href"), "The url is not identical to the target url"
        print(f"After pressing button {butt_name}")
        print("The url identical to the target url")
        print(button.get_attribute("href"))
        print()


#TC .. testing main page button's availability and function

print("TC .. testing main page button's availability and function\n")

button_test(butts)
home_butt.click()

print("Test passed!")

driver.close()
