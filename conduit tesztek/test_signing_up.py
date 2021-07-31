# Testing the "sign up" function with valid and invalid username, password and email
# data
# ...................................................................................

# environment
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# from random import randint
import pytest
# import requests
import time

options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "http://localhost:1667/"

# general settings for getting to sign_up window

driver.get(url)
main_butts = driver.find_elements_by_xpath('//*[@id="app"]/nav/div/ul/li/a')
main_butts[2].click()

# on the "sign_up" page

elements_xpath = '//*[@id="app"]/div/div/div/div/form/'
input_xpath = elements_xpath + 'fieldset/input'
signup_butt = driver.find_element_by_xpath(elements_xpath + 'button')

# generating test data - to bee fed into

# the following data could have been randomly generated (or could be on run), but at the moment I have
# no time to find out how

# username - no restrictions (must not be empty)
bad_users = [""]
good_users = ["testuserX", 1, "testuser1"]

# email - standard email form (must not be empty)

bad_email = ["", "aaa", "abc.hu", "a@hu", "a@test.", "a@.hu", "a@b.h"]
good_email = ["testuser@domain.uk"]

# passwords - eight character long containing at least one uppercase letter, one lowercase letter,
#             one number

bad_passws = ["",12345678, "1Aabcde", "11111111", "ABCDEFGH", "Abcdefgh", "abcdefg1"]
good_passws = ["Abcdefg1", "@Abcdef1"]


# functions

# finding input elements
def input_elements_list(xpath):
    input_elements = driver.find_elements_by_xpath(xpath)
    return input_elements


# finding input elements names for further use
def input_elements_names(element_list):
    input_names = []
    for i in range(len(element_list)):
        input_name = input_elements[i].get_attribute("placeholder")
        input_names.append(input_name)
    return input_names


# filling in input fields with test data
def fill_up_input_fields(un, em, pw):
    for j in range(len(input_names)):
        input_name = input_names[j]
        if input_name == "Username":
            input_elements[j].click()
            input_elements[j].clear()
            input_elements[j].send_keys(un)
        if input_name == "Email":
            input_elements[j].click()
            input_elements[j].clear()
            input_elements[j].send_keys(em)
        if input_name == "Password":
            input_elements[j].click()
            input_elements[j].clear()
            input_elements[j].send_keys(pw)

def test_data(un_v, em_v, pw_v):
    # empties
    test_data_result = []
    if un_v == "empty": test_un = ""
    test_data_result.append(test_un)
    if em_v == "empty": test_em = ""
    test_data_result.append(test_em)
    if pw_v == "empty": test_pw = ""
    test_data_result.append(test_pw)
    # good entry data
    #if un_v == "good":
        #for i in range(len(good_users)):
            #v = randint(0,len(good_users))
        #test_un = good_users[v]
    #if

    return test_un, test_em, test_pw


#def triplet():
    #values_triplet = []
    #values = []
    #value_list = ["empty", "good", "bad"]
    #for i in range(len(value_list)):
        #values[i] = (value_list[i])
        #values[i+1] = (value_list[i+1])
        #values.append(value_list[i+2])
        #values_triplet.append(values)

#triplet()


input_elements = input_elements_list(input_xpath)
input_names = input_elements_names(input_elements)

test_un, test_em, test_pw = test_data("good","empty","empty")

fill_up_input_fields(test_un,test_em,test_pw)

#signup_butt.click()

# Testing different input fields with different test datas
