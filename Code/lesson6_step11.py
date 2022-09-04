from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
link2 = 'http://suninjuly.github.io/registration2.html'
# Testing 1st link
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    element1 = browser.find_element(By.XPATH, "//input[@required and contains(@class,\"first\")]")
    element1.send_keys("Мой ответ")
    element2 = browser.find_element(By.XPATH, "//input[@required and contains(@class,\"second\")]")
    element2.send_keys("Мой ответ")
    element3 = browser.find_element(By.XPATH, "//input[@required and contains(@class,\"third\")]")
    element3.send_keys("Мой ответ")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# Testing 2nd link
try:
    browser = webdriver.Chrome()
    browser.get(link2)

    # Ваш код, который заполняет обязательные поля
    element1 = browser.find_element(By.XPATH, "//input[@required and contains(@class,\"first\")]")
    element1.send_keys("Мой ответ")
    element2 = browser.find_element(By.XPATH, "//input[@required and contains(@class,\"second\")]")
    element2.send_keys("Мой ответ")
    element3 = browser.find_element(By.XPATH, "//input[@required and contains(@class,\"third\")]")
    element3.send_keys("Мой ответ")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
