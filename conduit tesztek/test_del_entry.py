# Testing deletion of an article entry
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

# PREPARATIONS FOR GETTING TO "New Article" WINDOW

url = "http://localhost:1667/#/login"   # one must be signed in to be able to delete the new entry 
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

def article_id(element_id): # can be 'last' or a figure (index of element in a list)
    if element_id == 'last':
        saved_arts = elements_list_by_pass(saved_arts_path)
        element_to_del = saved_arts[len(saved_arts) - 1]
        return element_to_del
    else:
        saved_arts = elements_list_by_pass(saved_arts_path)
        element_to_del = saved_arts[int(element_id)]
        return element_to_del

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

pub_butt_pass = '//*[@id="app"]/div/div/div/div/form/button'
del_butt_path = '//*[@id="app"]/div/div[1]/div/div/span/button'
#del_message_path = '/html/body/div[2]/div/div'

saved_arts_path = '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div'

# variables

email = "laci@cond.com"
passwd = "ABcd123&"

title = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 7))
summary = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 10))
main = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 30))
tag = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 30))

text_list = [title, summary, main, tag]

# messages

message1 = "The new article's ID data (the last in the article list): \n"
message2 = "The last article's ID data after deleting the newly entered one: \n"
message3 = "The previously entered data have been deleted !"
message4 = "Test passed ! "
err_message1 = "Test failed ! The the two IDs are identical !"

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

 # deleting the new article

new_id = article_id('last').text

assign_del_el = ActionChains(driver).move_to_element(article_id('last')).click().perform()
time.sleep(1)
element_by_path(del_butt_path).click()
del_message = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div')))
time.sleep(2)
last_id = article_id('last').text
assert new_id != last_id, err_message1
print()
print(f"{message1}\n{new_id}")
print()
print(f"{message2}\n{last_id}")
print()
print(message3)
print(message4)

driver.quit()






