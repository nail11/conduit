from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
from random import randint
from selenium.webdriver.chrome.options import Options

options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


url = "http://localhost:1667/"

driver.get(url)
home_window = driver.window_handles[0]
butts = driver.find_elements_by_xpath('//*[@id="app"]/nav/div/ul/li/a')


def main_butts_activate(xpath):

    time.sleep(1)
    xpath.click()
    time.sleep(1)
    assert driver.current_url == xpath.get_attribute("href")


for i, button in enumerate(butts):
    main_butts_activate(butts[i])
    driver.switch_to.window(home_window)


#driver.close()