import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/file_input.html'

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    fname_field = browser.find_element(By.NAME, 'firstname')
    lname_field = browser.find_element(By.NAME, 'lastname')
    email_field = browser.find_element(By.NAME, 'email')
    file_input = browser.find_element(By.ID, 'file')
    submit = browser.find_element(By.CLASS_NAME, 'btn')

    fname_field.send_keys('text')
    lname_field.send_keys('text2')
    email_field.send_keys('text@text.com')
    file_input.send_keys(file_path)

    submit.click()

    time.sleep(10)
    browser.quit()

finally:
    time.sleep(5)
    browser.quit()