
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
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "http://localhost:1667/"

# general settings

driver.get(url)
butts = driver.find_elements_by_xpath('//*[@id="app"]/nav/div/ul/li/a')
home_butt = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[1]')

def main_butts_activate(button):
    button.click()
    time.sleep(1)


def button_test(butts):
    for i, button in enumerate(butts):
        button = butts[i]
        main_butts_activate(button)
        assert driver.current_url == button.get_attribute("href"), "A az url nem egyezik a cél url-el"
        print(driver.title)
        print("Az url egyezik a cél url-el")
        print(button.get_attribute("href"))


#TC .. testing button's present and activity

button_test(butts)

home_butt.click()

#TC .. testing




#driver.close()
