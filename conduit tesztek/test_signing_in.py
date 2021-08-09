# Testing the "sign in" function with valid and invalid data.
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
import nuts_and_bolts

options = Options()

#options.add_argument('--headless')
#options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "http://localhost:1667/"

# general settings for getting to sign_up window

driver.get(url)

decline = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[1]')
#decline.click()

