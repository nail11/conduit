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

options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# general settings for getting to "New Article" window

url = "http://localhost:1667/#/editor"

driver.get(url)

# main_butts = driver.find_elements_by_xpath('//*[@id="app"]/nav/div/ul/li/a')
# main_butts[2].click()

# data - elements, variables etc.

# elements

# input elements

art_title_text = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
art_summ_text = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input')
art_body_text = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
art_tag_text = driver.find_element_by_xpath(
    '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input')
pub_butt = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')

# saved text containers

title_cont_path = '/html/body/div[1]/div/div[1]/div/h1'
main_text_cont_path = '//*[@id="app"]/div/div[2]/div[1]/div/div[1]/p'
tag_cont_path = '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/a'

# messages

message01 = "Article title: "
message02 = "Article body text: "
message03 = "Article tag: "
message1 = "The saved (entry) data and the test data are identical !"
message2 = "Test passed ! "
err_message1 = "Test failed ! The saved (entry) data and the test data are not identical !"

# test data

title_text = "A Tisza"
summ_text = "Petőfi Sándor verse"
main_text = "\n Nyári napnak alkonyúlatánál.\n Megállék a kanyargó Tiszánál\n Ott, hol a kis Túr " \
            "siet beléje,\n Mint a gyermek anyja kebelére."
tag_text = "vers"


# functions

def element_by_path(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element


def text_feeding_in(text, field):
    for letter in text:
        field.send_keys(letter)


# Test

text_feeding_in(title_text, art_title_text)
text_feeding_in(summ_text, art_summ_text)
text_feeding_in(main_text, art_body_text)
text_feeding_in(tag_text, art_tag_text)
pub_butt.click()
time.sleep(1)
assert title_text == element_by_path(title_cont_path).text, err_message1
print(message01, message1)
main_text1 = main_text.replace('\n', "")
assert main_text1.strip() == element_by_path(main_text_cont_path).text, err_message1
print(message02, message1)
assert tag_text == element_by_path(tag_cont_path).text, err_message1
print(message03, message1)
print()
print(message2)

driver.close()
