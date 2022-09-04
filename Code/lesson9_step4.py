import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/alert_accept.html'

#current_dir = os.path.abspath(os.path.dirname(__file__))
#file_path = os.path.join(current_dir, 'file.txt')
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Open browser and get the link
    browser = webdriver.Chrome()
    browser.get(link)
    # Finding button and clicking
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
    # Switch to alert and accept it
    alert = browser.switch_to.alert
    alert.accept()
    #Find element contains variable x
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(int(x))
    # Find element with answer field and send_keys
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(y)
    # Press submit button
    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()
    # Switch to alert and get text from it (and accept)
    value = browser.switch_to.alert
    value_text = value.text
    value.accept()
    # Get text, split by : + space and get last value
    i = value_text.split(': ')[-1]

    time.sleep(3)
    #browser.quit()
    print(i)

    time.sleep(3)
    browser.quit()

finally:
    time.sleep(5)
    browser.quit()