# Testing the "sign in" function with valid and invalid data. Successful signing in finally.
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

options = Options()

options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "http://localhost:1667/#/login"

# general settings for getting to sign_in window

driver.get(url)

# data - elements, variables etc.

    # element's locations

email_input = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
password_input = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'

window_title_path = '//*[@id="app"]/div/div/div/div/h1'
input_butt_path = '//*[@id="app"]/div/div/div/div/form/button'

warn_window_title_path = "/html/body/div[2]/div/div[2]"
warn_text_path = "/html/body/div[2]/div/div[3]"
warn_accept_path = "/html/body/div[2]/div/div[4]/div/button"

user_name_path = "/html/body/div[1]/nav/div/ul/li[4]/a"

    # messages

email_req = "Email field required."
pass_req = "Password field required."
invalid_email = "Email must be a valid email."
invalid_data ="Invalid user credentials."
success = "Successful signing in !!\n" \
          "Test passed !"

    # test data

emails = ["","test@.","na@test.hu", "testuser1@example.com"]
passwds = ["", "a23in3kl", "1C56rt@$", "Abcd123$"]

    # lists

win_elements = [warn_window_title_path, warn_text_path, warn_accept_path]
message_elements = [email_req, invalid_email, invalid_data, pass_req ]


# function

def element_by_path(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element

# Test cases

if element_by_path(window_title_path).text == "Sign in":
    email = ""
    for email in emails:

        if email == emails[0]:
            element_by_path(email_input).clear()
            element_by_path(email_input).send_keys(emails[0])
            element_by_path(password_input).clear()
            element_by_path(password_input).send_keys(passwds[2])
            element_by_path(input_butt_path).click()
            time.sleep(1)
            assert element_by_path(win_elements[1]).text == message_elements[0]
            print(f"Test data: email= '{emails[0]}', password (acceptable)= '{passwds[2]}'")
            print(element_by_path(win_elements[0]).text)
            print(element_by_path(win_elements[1]).text)
            print()

            element_by_path(warn_accept_path).click()

        if email == emails[1]:
            element_by_path(email_input).clear()
            element_by_path(email_input).send_keys(emails[1])
            element_by_path(password_input).clear()
            element_by_path(password_input).send_keys(passwds[2])
            element_by_path(input_butt_path).click()
            time.sleep(1)
            assert element_by_path(win_elements[1]).text == message_elements[1]
            print(f"Test data: email= '{emails[1]}', password (acceptable)= '{passwds[2]}'")
            print(element_by_path(win_elements[0]).text)
            print(element_by_path(win_elements[1]).text)
            print()

            element_by_path(warn_accept_path).click()

        if email == emails[2]:
            element_by_path(email_input).clear()
            element_by_path(email_input).send_keys(emails[2])
            element_by_path(password_input).clear()
            element_by_path(password_input).send_keys(passwds[2])
            element_by_path(input_butt_path).click()
            time.sleep(1)
            assert element_by_path(win_elements[1]).text == message_elements[2]
            print(f"Test data: email= '{emails[2]}', password (acceptable)= '{passwds[2]}'")
            print(element_by_path(win_elements[0]).text)
            print(element_by_path(win_elements[1]).text)
            print()

            element_by_path(warn_accept_path).click()

        if email == emails[3]:
            element_by_path(email_input).clear()
            element_by_path(email_input).send_keys(emails[2])
            element_by_path(password_input).clear()
            element_by_path(password_input).send_keys(passwds[2])
            element_by_path(input_butt_path).click()
            time.sleep(1)
            assert element_by_path(win_elements[1]).text == message_elements[2]
            print(f"Test data: email= '{emails[3]}', password (acceptable)= '{passwds[2]}'")
            print(element_by_path(win_elements[0]).text)
            print(element_by_path(win_elements[1]).text)
            print()

            element_by_path(warn_accept_path).click()

    element_by_path(email_input).clear()
    element_by_path(email_input).send_keys(emails[3])

    passwd = ""
    for passwd in passwds:

        if passwd == passwds[0]:
            element_by_path(password_input).clear()
            element_by_path(password_input).send_keys(passwds[0])
            element_by_path(input_butt_path).click()
            time.sleep(1)
            assert element_by_path(win_elements[1]).text == message_elements[2]
            print(f"Test data: email (acceptable)= '{emails[3]}', password = '{passwds[0]}'")
            print(element_by_path(win_elements[0]).text)
            print(element_by_path(win_elements[1]).text)
            print()

            element_by_path(warn_accept_path).click()

        if passwd == passwds[1]:
            element_by_path(password_input).clear()
            element_by_path(password_input).send_keys(passwds[1])
            element_by_path(input_butt_path).click()
            time.sleep(1)
            assert element_by_path(win_elements[1]).text == message_elements[2]
            print(f"Test data: email (acceptable)= '{emails[3]}', password = '{passwds[1]}'")
            print(element_by_path(win_elements[0]).text)
            print(element_by_path(win_elements[1]).text)
            print()

            element_by_path(warn_accept_path).click()

        if passwd == passwds[2]:
            element_by_path(password_input).clear()
            element_by_path(password_input).send_keys(passwds[2])
            element_by_path(input_butt_path).click()
            time.sleep(1)
            assert element_by_path(win_elements[1]).text == message_elements[2]
            print(f"Test data: email (acceptable)= '{emails[3]}', password = '{passwds[2]}'")
            print(element_by_path(win_elements[0]).text)
            print(element_by_path(win_elements[1]).text)
            print()

            element_by_path(warn_accept_path).click()

        if passwd == passwds[3]:
            element_by_path(password_input).clear()
            element_by_path(password_input).send_keys(passwds[3])
            element_by_path(input_butt_path).click()
            time.sleep(1)
            assert element_by_path(user_name_path).is_displayed()
            assert element_by_path(user_name_path).text == emails[3][0:9]
            print(f"Test data: email (acceptable)= '{emails[3]}', password = '{passwds[3]}'")
            print(f"User name: {emails[3][0:9]}")
            print(success)
driver.close()





