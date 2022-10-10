import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
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
        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text,
            "Should be Congratulations with registration"
        )

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
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
        self.assertEqual(
            "Congratulations! You have successfully registered!" == welcome_text,
            "Should be Congratulations with registration"
        )


if __name__ == '__main__':
    unittest.main()
