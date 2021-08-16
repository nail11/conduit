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

#options.add_argument('--headless')
#options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "http://localhost:1667/#/login"

# general settings for getting to sign_in window

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


# ..input elements

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

title_text = ""
summ_text = ""
main_text = ""
tag_text = ""

# ..setting up environment

sign_in()
time.sleep(1)
#saved_arts = elements_list_by_pass(saved_arts_path)
element_by_path(new_art_butt_path).click()
wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, title_path)))

# obtaining test data (text to save in Conduit)

with open("upload_text.txt", "r", encoding="utf-8") as text:
    text_to_upload1 = text.readline()
    text_to_upload2 = text.readline()
    text_to_upload3 = text.readline()
    text_to_upload4 = text.readline()
    text_to_upload5 = text.readline()
    text_to_upload6 = text.readline()
    text_to_upload7 = text.readlines()

title_text = text_to_upload3.split()
summ_text =  text_to_upload1+text_to_upload3+","+text_to_upload5
main_text =  text_to_upload7
tag_text = "vers"

#.. creating new article

#text_list = [title_text,summ_text, main_text, tag_text]

driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[1]/input').send_keys(title_text)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[2]/input').send_keys(summ_text)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[3]/textarea').send_keys(main_text)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input').send_keys(tag_text)





#wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')))
#field_list = [element_by_path(title_path), element_by_path(summ_path), element_by_path(main_path), element_by_path(tag_path)]
#for i in range(len(field_list)):
   # field_list[i].send_keys(text_list[i])
   # time.sleep(2)
#element_by_path(pub_butt_path).click()

#new_article(text_list, field_list)
element_by_path(home_butt_path).click()
time.sleep(1)



###########################################################################################################x
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


email = "laci@cond.com"
passwd = "ABcd123&"

driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(email)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys(passwd)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')))
time.sleep(2)
#driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[1]/input').send_keys('a')
#ew_art_butt_path = '//*[@id="app"]/nav/div/ul/li[2]/a'

driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[1]/input').send_keys('a')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[2]/input').send_keys('b')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[3]/textarea').send_keys('c')
time.sleep(1)

driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input').send_keys('d')

time.sleep(1)#########################################################################x