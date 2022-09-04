import selenium.webdriver.support.ui
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


link = 'http://suninjuly.github.io/selects1.html'
# Testing 1st link
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который находит значение х, считает функцию и вводит в нужное поле

    element = browser.find_element(By.CSS_SELECTOR, 'select#dropdown')
    x1 = browser.find_element(By.CSS_SELECTOR, 'span#num1').text
    x2 = browser.find_element(By.CSS_SELECTOR, 'span#num2').text

    select = selenium.webdriver.support.ui.Select(element)
    select.select_by_value(str(int(x1)+int(x2)))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    print(x1,x2)
