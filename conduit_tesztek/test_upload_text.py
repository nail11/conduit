#environment
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
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
driver.maximize_window()

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

def new_article_by_letter(source_list,field_list):
    for i in range(len(source_list)):
        text_feeding_in(source_list[i],field_list[i])
    element_by_path(pub_butt_path).click()

def new_article_by_text(source_list,field_list):
    for i in range(len(source_list)):
        field_list[i].send_keys(source_list[i])
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

# web elements
    # ..main window and input elements

home_butt_path = '//*[@id="app"]/nav/div/ul/li[1]'
new_art_butt_path = '//*[@id="app"]/nav/div/ul/li[2]/a'
saved_arts_path = '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div'

email_input_path = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
password_input_path = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
input_butt_path = '//*[@id="app"]/div/div/div/div/form/button'

    # ..elements for editing and retrieving

title_path = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
summ_path = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
main_path = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
tag_path = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'

main_text_cont_path = '//*[@id="app"]/div/div[2]/div[1]/div/div[1]/p'
pub_butt_path = '//*[@id="app"]/div/div/div/div/form/button'

# variables, test data

email = "laci@cond.com"
passwd = "ABcd123&"

title_text = ""
summ_text = ""
main_text = ""
tag_text = ""
new_art_id = ""
new_main_text = ""

# messages

message1 = "Test ...... - new entry from text file\n"
message2 = "The new article has been saved !"
message3 = f"The new artile's ID is:  "
message4 = "The saved text and the uploaded text are identical ! The texts are: "
message5 = "Test passed !"
err_message1 = "No new article !"
err_message2 = "The saved text and the uploaded text are not identical !"

# TEST

# ..setting up environment

sign_in()
time.sleep(1)
saved_arts1 = elements_list_by_pass(saved_arts_path)

# obtaining test data (text to save in Conduit)

with open("upload_text.txt", "r", encoding="utf-8") as text:
    text_to_upload1 = text.readline()
    text_to_upload2 = text.readline()
    text_to_upload3 = text.readline()
    text_to_upload4 = text.readline()
    text_to_upload5 = text.readline()
    text_to_upload6 = text.readline()
    text_to_upload7 = text.readlines()

title_text = text_to_upload3.strip()
summ_text =  f"{text_to_upload1.strip()} {text_to_upload3.strip()}, {text_to_upload5.strip()}"
main_text =  text_to_upload7
tag_text = "vers"

#.. creating new article

element_by_path(new_art_butt_path).click()
wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, title_path)))

text_list = [title_text,summ_text, main_text, tag_text]
field_list = [element_by_path(title_path), element_by_path(summ_path), element_by_path(main_path), element_by_path(tag_path)]

new_article_by_text(text_list, field_list)                              # creating new article
time.sleep(1)
new_main_text = element_by_path(main_text_cont_path).text
element_by_path(home_butt_path).click()

#.. checking existence of the new article

time.sleep(1)
saved_arts2 = elements_list_by_pass(saved_arts_path)
art_id = article_by_ord("last").text
new_art_id = art_id.replace('\n','')                                    # obtaining the ID of the new article
time.sleep(1)
assert len(saved_arts2) == len(saved_arts1)+1, err_message1             # comparing the number of articles
                                                                        # before and after
print()
print(message1)
print(message2)
print(f"{message3}{new_art_id}\n")
mod_main_text = ""
for i in range(len(main_text)):                                         # to make the two texts comparable
    mod_main_text = mod_main_text+main_text[i]
assert mod_main_text.replace('\n'," ") == new_main_text, err_message2   # comparing uploaded and saved texts
print(f"{message4}\n{new_main_text}\n")
print(message5)

driver.quit()
