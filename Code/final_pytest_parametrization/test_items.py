import time

from selenium.webdriver.common.by import By


def test_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    # time.sleep(5)
    button = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert len(button) > 0, 'Кнопка не найдена'
