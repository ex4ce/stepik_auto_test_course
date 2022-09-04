from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = 'https://suninjuly.github.io/math.html'
# Testing 1st link
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который находит значение х, считает функцию и вводит в нужное поле
    element1 = browser.find_element(By.XPATH, "//div//span[@id=\"input_value\"]")
    element2 = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    element3 = browser.find_element(By.ID, "robotsRule")
    result_field = browser.find_element(By.CSS_SELECTOR, "input[id=\"answer\"]")
    # Считаем
    x = element1.text
    y=calc(x)
    # Отмечаем поля
    element2.click()
    element3.click()
    result_field.send_keys(y)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
