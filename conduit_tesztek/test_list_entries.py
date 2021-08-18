# TC 21 - Making and printing out a list of a particular user's articles
#
# ...................................................................................

# environment
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import random
import pytest
import time
import string
import conduitdata

options = Options()

options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# PREPARATIONS FOR GETTING TO "user" WINDOW

url = "http://localhost:1667/#/login"   # one must be signed in to be able to modify the new entry
                                        # and to fulfil the precondition

driver.get(url)

# functions

def sign_in():
    element_by_path(email_input_path).send_keys(email)
    element_by_path(password_input_path).send_keys(passwd)
    element_by_path(input_butt_path).click()
    #time.sleep(1)

def element_by_path(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element

def elements_list_by_pass(xpath):
    elements_list = driver.find_elements_by_xpath(xpath)
    return elements_list

def text_feeding_in(text, field):
    for letter in text:
        field.send_keys(letter)

def new_article(source_list,field_list):
    for i in range(len(source_list)):
        text_feeding_in(source_list[i],field_list[i])
    element_by_path(pub_butt_path).click()

def article_by_ord(element_id): # element_id can be 'last' or a figure (index of element in a list)
    if element_id == 'last':
        saved_arts = elements_list_by_pass(saved_arts_path)
        element_chosen = saved_arts[len(saved_arts) - 1]
        return element_chosen
    else:
        saved_arts = elements_list_by_pass(saved_arts_path)
        element_chosen = saved_arts[int(element_id)]
        return element_chosen

#..elements for setting up environment and on different pages

home_butt_path = '//*[@id="app"]/nav/div/ul/li[1]'
new_art_butt_path = '//*[@id="app"]/nav/div/ul/li[2]/a'
user_butt_path ='//*[@id="app"]/nav/div/ul/li[4]'

email_input_path = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
password_input_path = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
input_butt_path = '//*[@id="app"]/div/div/div/div/form/button'

title_path = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
summ_path = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
main_path = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
tag_path = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'

pub_butt_path = '//*[@id="app"]/div/div/div/div/form/button'
del_butt_path = '//*[@id="app"]/div/div[1]/div/div/span/button'
edit_butt_path = '//*[@id="app"]/div/div[1]/div/div/span/a'

favorit_but_path ='//*[@id="app"]/div/div[2]/div/div/div[1]/ul/li[2]/a'
my_art_path = '//*[@id="app"]/div/div[2]/div/div/div[1]/ul/li[1]/a'
saved_arts_path = '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div'
users_art_path = '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div'

# variables, test data

email = "laci@cond.com"
passwd = "ABcd123&"

actual_user = ""
user_entries = []
saved_arts = []
users_articles = []

# messages

message1  = "The list of the user's articles has been completed !"
message2 = f"The user's articles' ID-s are attached to the articles_list.txt file !\n"
message3 = "Test passed ! "

err_message1 = "Test failed ! The number of all entries and the number of the users entries are identical !"
err_message2 = "Test failed ! The list of user's articles has not been completed !"

def test_list_entries():
# TEST

# ..setting up environment

    sign_in()
    time.sleep(1)

# Getting to the window containing the user's articles

    wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, user_butt_path)))
    user_butt = driver.find_element_by_xpath(user_butt_path)
    actual_user = user_butt.text
    saved_arts = elements_list_by_pass(saved_arts_path)
    user_butt.click()
    time.sleep(1)
    element_by_path(favorit_but_path).click()
    time.sleep(1)
    element_by_path(my_art_path).click()
    time.sleep(2)

# finding elements attached to the user

    user_entries = elements_list_by_pass('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div')

    assert len(user_entries) != len(saved_arts), err_message1

# making list of the user's elements ID-s

    for i in range(len(user_entries)):
        if actual_user in user_entries[i].text:
            users_articles.append(user_entries[i].text)

    assert len(users_articles) == len(user_entries), err_message2
    print("TC 20 - listing and printing out entries")
    print()
    print(message1)

# opening a text file and sending the list

    with open("articles_list.text", "a", encoding="utf-8") as arts:
        for i, element in enumerate(users_articles):
            arts.write(f"{i+1}.,\n{element}\n\n")
    print()
    print(message2)
    print(message3)
    driver.quit()


