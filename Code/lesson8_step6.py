from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = 'http://suninjuly.github.io/execute_script.html'
# Testing 1st link
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который находит значение х, считает функцию и вводит в нужное поле
    element1 = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    element2 = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    element3 = browser.find_element(By.ID, "robotsRule")
    result_field = browser.find_element(By.CSS_SELECTOR, "input[id=\"answer\"]")
    x = element1.text
    # Считаем
    y=calc(x)
    # Отмечаем поля
    result_field.send_keys(y)
    browser.execute_script("return arguments[0].scrollIntoView(true);", element2)
    element2.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", element3)
    element3.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
