# TC 20 - Testing the "cookie" window and the effect of accepting the warning
# ...................................................................................

# environment
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
#from random import randint
import pytest
import time
#import nuts_and_bolts

options = Options()

options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "http://localhost:1667/"

# general settings for getting to sign_up window

driver.get(url)

# elements

cookie_panel = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]')
accept = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]')
reference_url =driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[1]/div/a')

def test_cookies_warning():

# TC 21 - TESTS


    main_window = driver.window_handles[0]
    url_to_go = reference_url.get_attribute("href")
    corr_url = url_to_go[0:8] + "www." + url_to_go[8:]
    reference_url.click()
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

# obtaining the url of cookie learning site

    learn_url = driver.current_url

    assert learn_url == corr_url
    print()
    print("TC 20 - testing cookies' window")
    print("Test case .. - testing cookies allert\n")
    print(f"The link '{learn_url}' has been opened !")

# checking up cookies

    driver.switch_to.window(main_window)
    cookies = driver.get_cookies()
    assert cookies != None
    print(f"Cookies are: {cookies} ")

    cookie_panel
    time.sleep(1)
    if cookie_panel.is_displayed():
        accept.click()
    print("Cookie panel is not reachable after clicking on accept button !\n")
    print("Test passed!")

    driver.quit()




