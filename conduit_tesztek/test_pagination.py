# Testing of moving between pages containing articles
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

#..elements for setting up environment and on different pages

home_butt_path = '//*[@id="app"]/nav/div/ul/li[1]'
new_art_butt_path = '//*[@id="app"]/nav/div/ul/li[2]/a'
nav_butts_path = '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/nav/ul/li/a'
nav_butt_path = '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/nav/ul/li[1]/a'


email_input_path = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
password_input_path = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
input_butt_path = '//*[@id="app"]/div/div/div/div/form/button'

saved_arts_path = '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div'

# variables, test data

email = "laci@cond.com"
passwd = "ABcd123&"

title_text = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 7))
summary_text = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 10))
main_text = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 30))
tag_text = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 5))

text_list = [title_text, summary_text, main_text, tag_text]

nav_butt_texts = []
elements_on_page = []

# messages

message1 = "TC.. going around the pages \n"
message2 = f"The necessary  number of pages and the number of navigation buttons are equal !"
message3 = f"The calculated number of entries on the last page and the counted number of entries on the last page are equal !"
message4 = f"The ID of the last element and the ID of the last page's last element are identical !"
message5 = "Test passed ! "

err_message1 = "Test failed ! The the two data are not identical !"

# TEST

# ..setting up environment
def test_pagination():
    sign_in()
    time.sleep(1)

# .. collecting data from the app

    art_entries0 = elements_list_by_pass(saved_arts_path)
    art_entries_num0 = len(art_entries0)
    nav_butts = elements_list_by_pass(nav_butts_path)
    nav_butt_num = len(nav_butts)
    last_art_entries0_id = art_entries0[art_entries_num0-1].text

# turning page by clicking on navigation buttons and count element on the pages

    for i in range(nav_butt_num):
        nav_butts[i].click()
        time.sleep(1)
        art_entries1= elements_list_by_pass(saved_arts_path)
        art_entries_num1 = len(art_entries1)
        last_art_entries1_id = art_entries1[art_entries_num1 - 1].text
        elements_on_page.append(art_entries_num1)

# calculating test data, based on the number of entries which can be compared with the real data

    page_num_shouldbe = art_entries_num0//10+1                          # calculating page numbers
    last_page_art_num = art_entries_num0%10                             # calculating the  number of entry  on the last page
    elements_on_last_page = elements_on_page[len(elements_on_page)-1]

    assert page_num_shouldbe == nav_butt_num
    assert last_page_art_num == elements_on_last_page
    assert last_art_entries0_id == last_art_entries1_id

    print()
    print(message1)
    print()
    print(message2)
    print(f"{page_num_shouldbe} == {nav_butt_num}\n")
    print(message3)
    print(f"{last_page_art_num} == {elements_on_last_page}\n")
    print(message4)
    print(f"{last_art_entries0_id} \n == \n {last_art_entries1_id}\n")
    print(message5)

    driver.close()