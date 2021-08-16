# Testing the action of adding a new article entry
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
#from random import randint
import random
import pytest
import time
import string

#import nuts_and_bolts

options = Options()

options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# PREPARATIONS FOR GETTING TO "New Article" WINDOW

url = "http://localhost:1667/#/login"   # one must be signed in to make the search for new entry possible
                                        # or, in other words, to fulfil the precondition

driver.get(url)

#..elements for setting up environment

saved_texts_path = '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div'
new_art_butt_path = '//*[@id="app"]/nav/div/ul/li[2]/a'

email_field = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
passw_field = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
input_butt = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
new_art_butt =driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')

email = "laci@cond.com"
passwd = "ABcd123&"

saved_texts1 = []

# ..setting up environment

email_field.send_keys(email)
passw_field.send_keys(passwd)
input_butt.click()
time.sleep(1)
saved_texts1 = driver.find_elements_by_xpath(saved_texts_path)
new_art_butt.click()
time.sleep(1)

# MAIN TASK

# data - elements, variables etc.

#.. elements

#..main window elements

home_but_path = '//*[@id="app"]/nav/div/ul/li[1]/a'

#..input elements

art_title_text = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
art_summ_text = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input')
art_body_text = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
art_tag_text = driver.find_element_by_xpath(
    '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input')
 
pub_butt = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')

# ..containers for saved text

title_cont_path = '/html/body/div[1]/div/div[1]/div/h1'
main_text_cont_path = '//*[@id="app"]/div/div[2]/div[1]/div/div[1]/p'
tag_cont_path = '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/a'

# messages

message01 = "Article title: "
message02 = "Article body text: "
message03 = "Article tag: "
message1 = "The entry data and the test data are identical !"
message2 = "Az új bejegyzés elmentve:\n\n"
message3 = "Test passed ! "
err_message1 = "Test failed ! The saved (entry) data and the test data are not identical !"
err_message2 = "Test failed ! New entry hasn't been created !"

# test data

#title_text = "A Tisza"
#summ_text = "Petőfi Sándor verse"
#main_text = "\n Nyári napnak alkonyúlatánál.\n Megállék a kanyargó Tiszánál\n Ott, hol a kis Túr " \
#            "siet beléje,\n Mint a gyermek anyja kebelére."
#tag_text = "vers"

title_text = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 7))
summ_text = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 10))
main_text = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 30))
tag_text = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 5))

# variables

saved_texts2 = []

# functions

def sign_in():
    element_by_path(email_input_path).send_keys(email)
    element_by_path(password_input_path).send_keys(passwd)
    element_by_path(input_butt_path).click()
    time.sleep(1)

def element_by_path(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element

def text_feeding_in(text, field):
    for letter in text:
        field.send_keys(letter)

# TEST

text_feeding_in(title_text, art_title_text)
text_feeding_in(summ_text, art_summ_text)
text_feeding_in(main_text, art_body_text)
text_feeding_in(tag_text, art_tag_text)

pub_butt.click()
time.sleep(1)
print()
assert title_text == element_by_path(title_cont_path).text, err_message1
print(message01, message1)
main_text1 = main_text.replace('\n', "")
assert main_text1.strip() == element_by_path(main_text_cont_path).text, err_message1
print(message02, message1)
assert tag_text == element_by_path(tag_cont_path).text, err_message1
print(message03, message1)
print()

element_by_path(home_but_path).click()
time.sleep(1)
saved_texts2 = driver.find_elements_by_xpath(saved_texts_path)
assert len(saved_texts2) == len(saved_texts1)+1, err_message2
saved_text2 = saved_texts2[len(saved_texts2)-1]
print(message2+saved_text2.text)
print()
print(message3)

driver.quit()
