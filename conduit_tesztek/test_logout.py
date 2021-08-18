# TC 18 - Testing the "log out" function with using the elements displaying on the head the window before
# and after loging out
# ...................................................................................

# environment
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#from random import randint
import pytest
import time

# import nuts_and_bolts

options = Options()

options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# general settings for getting to sign_up window

url = "http://localhost:1667/#/login"

driver.get(url)

# data - elements, variables etc.

# element's locations

email_input = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
password_input = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
input_butt = '//*[@id="app"]/div/div/div/div/form/button'
log_out_butt = '//*[@id="app"]/nav/div/ul/li[5]/a'
head_butt_selector = "li"

# test data

buttons1 = []  # buttons in the head of the main window before log out
buttons2 = []  # buttons in the head of the main window after log out

# input data

email = "testuser1@example.com"
passw = 'Abcd123$'

# others

message1 = "Buttons on the head of the window before loging out: "
message2 = "Buttons on the head of the window after loging out: "
message3 = "Successful loging out ! Test passed !"


# function

def element_by_path(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element


def element_by_selector(sel):
    element = driver.find_elements_by_css_selector(sel)
    return element

def test_logout():

# Test

    element_by_path(email_input).send_keys(email)
    element_by_path(password_input).send_keys(passw)
    element_by_path(input_butt).click()

    time.sleep(1)
    head_butts1 = element_by_selector(head_butt_selector)
    for button1 in head_butts1:
        buttons1.append(button1.text)

    logout_button = element_by_path(log_out_butt)

    if logout_button.is_displayed():
        logout_text = logout_button.text
        logout_button.click()

    time.sleep(1)
    head_butts2 = element_by_selector(head_butt_selector)
    for button2 in head_butts2:
        buttons2.append(button2.text)

    assert (logout_text in buttons1) and (logout_text not in buttons2)
    print('TC 18 - log out')
    print(message1)
    print(buttons1[0:5])
    print()
    print(message2)
    print(buttons2[0:3])
    print()
    print(message3)

    driver.close()
