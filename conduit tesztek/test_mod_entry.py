# Testing of the action of modifying an article entry
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

# PREPARATIONS FOR GETTING TO "/articles" WINDOW

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

def text_feeding_in(text, field):
    for letter in text:
        field.send_keys(letter)

def article_id(element_id): # element_id can be 'last' or a figure (index of element in a list)
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
#del_message_path = '/html/body/div[2]/div/div'

saved_arts_path = '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div'

# variables, test data

email = "laci@cond.com"
passwd = "ABcd123&"

title_text = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 7))
summary_text = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 10))
main_text = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 30))
tag_text = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 30))

text_list = [title_text, summary_text, main_text, tag_text]

# messages

message1 = "The character chain to be modify: \n"
message2 = "The character chain to be added: \n"
message3 = "The modified character chain: \n"
message4 = "Test passed ! "
err_message1 = "Test failed ! The the two entries are identical !"
err_message2 = "Test failed ! The the new entries does not contain the previous or/and the modifying text!"
# TEST

# ..setting up environment

sign_in()
time.sleep(1)

#.. entering new article

element_by_path(new_art_butt_path).click()
time.sleep(1)
field_list = [element_by_path(title_path), element_by_path(summ_path), element_by_path(main_path), element_by_path(tag_path)]
new_article(text_list, field_list)
element_by_path(home_butt_path).click()
time.sleep(1)

# choosing the newly entered article to modify

new_art = article_id('last')
assign_del_el = ActionChains(driver).move_to_element(new_art).click().perform()
time.sleep(1)

# modifying the newly entered article

element_by_path(edit_butt_path).click()
text_to_modify = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 30))
time.sleep(1)
text_feeding_in(text_to_modify, element_by_path(main_path))
element_by_path(pub_butt_path)

# read the contain of the "main-text" field ("element_by_path(main_path") and set up assertions

modified_text = element_by_path(main_path).get_attribute('value')

assert main_text != modified_text,err_message1
assert main_text in modified_text and text_to_modify in modified_text, err_message2
print()
print(f"{message1}{main_text}\n")
print(f"{message2}{text_to_modify}\n")
print(f"{message3}{modified_text}\n")
print(message4)
driver.quit()