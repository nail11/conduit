# Testing the creation of a new article
#
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

# import nuts_and_bolts

options = Options()

#options.add_argument('--headless')
#options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# general settings for getting to "New Article" window

url = "http://localhost:1667/#/editor"

driver.get(url)

main_butts = driver.find_elements_by_xpath('//*[@id="app"]/nav/div/ul/li/a')
main_butts[2].click()

# data - elements, variables etc.

    # elements

article_title_path = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
article_summ_path = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
article_body_path = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
article_tag_path = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'

    # messages

user_req = "Username field required."
email_req = "Email field required."
pass_req = "Password field required."
invalid_email = "Email must be a valid email."
invalid_pass = "Password must be 8 characters long and include 1 number, 1 uppercase letter, " \
               "and 1 lowercase letter."
reused_email = "Email already taken."
signup_success = "Your registration was successful!"

    # variables

field_val = []  # a list of "empty", "good", "bad" or "reused" according to the values
                # one would like to give the input fields. The order is "username", "email" and "password".
warning_title = "" # the title of the message window
warning_text = ""  # warning or message in the jumping up window

# elements on the "sign_up" page

elements_xpath = '//*[@id="app"]/div/div/div/div/form/'
input_xpath = elements_xpath + 'fieldset/input'
signup_butt = driver.find_element_by_xpath(elements_xpath + 'button')
