#environment
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
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

email = "laci@cond.com"
passwd = "ABcd123&"

driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(email)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys(passwd)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()

driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
time.sleep(2)
#driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[1]/input').send_keys('a')
driver.find_element_by_css_selector("//input[placeholder='Article Title']").send_keys('a')
time.sleep(1)
driver.find_element_by_xpath('//input[@placeholder = "What\'s this article about?"]').send_keys('b')
driver.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown"]').send_keys('c')


driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input').send_keys('d')

time.sleep(1)