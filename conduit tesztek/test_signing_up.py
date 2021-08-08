# Testing the "sign up" function with valid ("good") and invalid ("bad") username, password
# and email data
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

url = "http://localhost:1667/"

# general settings for getting to sign_up window

driver.get(url)
main_butts = driver.find_elements_by_xpath('//*[@id="app"]/nav/div/ul/li/a')
main_butts[2].click()


# data - elements, variables etc.

#reg_failed = "/html/body/div[2]/div/div[2]"
warn_window_path = "/html/body/div[2]/div"
warn_text_path = "/html/body/div[2]/div/div[3]"
warn_accept_path = "/html/body/div[2]/div/div[4]/div/button"
user_req = "Username field required."
email_req = "Email field required."
pass_req = "Password field required."
invalid_email = "Email must be a valid email."
invalid_pass = "Password must be 8 characters long and include 1 number, 1 uppercase letter, " \
               "and 1 lowercase letter."
reused_email = "Email already taken."

field_val = []  # a list of "empty", "good", "bad" or "reused" according to the values
                # one would like to give the input fields. The order is "username", "email" and "password".

    # elements on the "sign_up" page

elements_xpath = '//*[@id="app"]/div/div/div/div/form/'
input_xpath = elements_xpath + 'fieldset/input'
signup_butt = driver.find_element_by_xpath(elements_xpath + 'button')

# generating test data - test data dictionary ("test_data_source")

 # the following data could have been randomly generated (or could be on run), but at the moment I have
 # no time to find it out how
 #  Username - no restrictions (must not be empty)
 #  Email - standard email form (must not be empty)
 #  Passwords - eight character long, containing at least one uppercase letter, one lowercase letter,
 #              and one digit

test_data_source = {"Username": [["-"], ["testuserX", 1, "testuser1"]],
                    "Email": [["aaa", "abc.hu", "a@hu", "a@test.", "a@.hu", "a@b.h"], ["test@domain.uk","klm@no.nl" , "abc@def.hu"],
                              ["testuser@domain.uk", "testuser1@example.com", "testuser2@example.com", "testuser3@example.com", "w@rtz.bg"]],
                    "Password": [[12345678, "1Aabcde", "11111111", "ABCDEFGH", "Abcdefgh", "abcdefg1"],
                                 ["Abcdefg1", "@Abcdef1"], ["Abcd123$"]]
                    }

# functions

    # finding input field (elements)
def input_elements_list(xpath):
    input_elements = driver.find_elements_by_xpath(xpath)
    return input_elements

    # finding input element's names for further use (in an other app)
def input_elements_names(element_list):
    input_names = []
    for i in range(len(element_list)):
        input_name = input_elements[i].get_attribute("placeholder")
        input_names.append(input_name)
    return input_names

    # randomly getting test data for the "sign up" input fields from "empty", "good", "bad" and "reused" data pools
def get_test_data(field_val):
    result = []
    value = ""
    for i in range(len(input_names)):
        field = list(field_val)
        if field[i] == "empty":
            value = ""
        elif field[i] == "bad":
            data_list = list(test_data_source.values())
            data_source = data_list[i][0]
            v = randint(0, len(data_source) - 1)
            value = data_source[v]
        elif field[i] == "good":
            data_list = list(test_data_source.values())
            data_source = data_list[i][1]
            v = randint(0, len(data_source) - 1)
            value = data_source[v]
        elif field[i] == "reused":
            data_list = list(test_data_source.values())
            data_source = data_list[i][2]
            v = randint(0, len(data_source) - 1)
            value = data_source[v]
        result.append(value)
    return result

    # click, clear and send new data to the field in a list, specified by ind
def click_and_send(ind, data):
    input_elements[ind].click()
    input_elements[ind].clear()
    input_elements[ind].send_keys(data)

    # filling in input fields with test data
def fill_up_input_fields(un, em, pw):
    for j in range(len(input_names)):
        input_name = input_names[j]
        if input_name == "Username":
            click_and_send(j, un)
        if input_name == "Email":
            click_and_send(j, em)
        if input_name == "Password":
            click_and_send(j, pw)
            
# warning windows and messages ("Value_list" a list of 'empty' or 'bad' or 'good', the values
#                               corresponding with  entry values of 'test_data_list')
def warning(value_list):
    warning = driver.find_element_by_xpath(warn_window_path)
    global warning_text
    warning_text = driver.find_element_by_xpath(warn_text_path).text
    global warn_accept_butt
    warn_accept_butt = driver.find_element_by_xpath(warn_accept_path)
    if warning.is_displayed:
        #for i in range(len(value_list)):
        if value_list[0] == "empty":
            return user_req
        if value_list[1] == "empty":
            return email_req
        if value_list[2] == "empty":
            return pass_req
        if value_list[1] == "bad":
            return invalid_email
        if value_list[2] == "bad":
            return invalid_pass
        if value_list[1] == "reused":
            return reused_email
        #if value_list[2] == "reused":
            #return "Reused email"

try:
    # start testing under different conditions

    input_elements = input_elements_list(input_xpath)
    input_names = input_elements_names(input_elements)

    # TC 01 -  empty fields (all)
    field_val = ["empty", "empty", "empty"]
    test_data_list = get_test_data(field_val)

    fill_up_input_fields(test_data_list[0], test_data_list[1], test_data_list[2])
    time.sleep(1)
    signup_butt.click()
    time.sleep(2)

    assert warning(field_val) == warning_text

    print("TC01 - empty fields")
    print("Test passed - Message: " +warning_text)
    print( )
    warn_accept_butt.click()

    # TC 02 -  wrong e-mail, empty password

    field_val = ["good", "bad", "empty"]
    test_data_list = get_test_data(field_val)

    fill_up_input_fields(test_data_list[0], test_data_list[1], test_data_list[2])
    time.sleep(1)
    signup_butt.click()
    time.sleep(2)

    assert warning(field_val) == warning_text

    print("TC02 - wrong e_mail, empty password - empty field warning has priority")
    print("Test passed - Message: " + warning_text)
    print()
    warn_accept_butt.click()

    # TC 03 -  reused e-mail, good password

    field_val = ["good", "reused", "good"]
    test_data_list = get_test_data(field_val)

    fill_up_input_fields(test_data_list[0], test_data_list[1], test_data_list[2])
    time.sleep(1)
    signup_butt.click()
    time.sleep(4)

    assert warning(field_val) == warning_text

    print("TC03 - reused e_mail, good password")
    print("Test passed - Message: " + warning_text)
    print()
    warn_accept_butt.click()

    # TC 04 -  wrong e-mail, good password

    field_val = ["good", "bad", "good"]
    test_data_list = get_test_data(field_val)

    fill_up_input_fields(test_data_list[0], test_data_list[1], test_data_list[2])
    time.sleep(1)
    signup_butt.click()
    time.sleep(4)

    assert warning(field_val) == warning_text

    print("TC04 - wrong e_mail, good password")
    print("Test passed - Message: " + warning_text)
    print()
    warn_accept_butt.click()

    # TC 05 -  good e-mail, wrong password

    field_val = ["good", "good", "bad"]
    test_data_list = get_test_data(field_val)

    fill_up_input_fields(test_data_list[0], test_data_list[1], test_data_list[2])
    time.sleep(1)
    signup_butt.click()
    time.sleep(4)

    assert warning(field_val) == warning_text

    print("TC05 - good e_mail, wrong password")
    print("Test passed - Message: " + warning_text)
    print()
    warn_accept_butt.click()

finally:
    driver.close()
