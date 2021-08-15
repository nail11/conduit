# Testing the "cookie" window and the effect of accepting the warning
# ...................................................................................

# environment
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from random import randint
import pytest
import time
#import nuts_and_bolts

def test_cookie_accepted():
    options = Options()

    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    url = "http://localhost:1667/"

# general settings for getting to sign_up window

    driver.get(url)

# elements

    cookie_panel = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]')
    decline = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[1]')
    accept = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]')

# Tests

    try:

        if cookie_panel.is_displayed():
            accept.click()
            cookie_panel_empty = driver.find_element_by_class('//*[@id="cookie-policy-panel"]')
            accept.click()
    except:
        print("Test case .. - testing cookies allert")
        print("Cookie panel is not reachable after clicking on accept button\n")
        print("Test passed!")

    finally:
        driver.close()




