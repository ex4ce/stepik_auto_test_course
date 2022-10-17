import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

links = [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]


@pytest.mark.parametrize('lesson', links)
@pytest.mark.xpass
def test_stepik_lessons(browser, lesson):
    answer = math.log(int(time.time()) - 0.9)
    link = f'https://stepik.org/lesson/{lesson}/step/1'

    browser.implicitly_wait(10)
    browser.get(link)

    textarea = browser.find_element(By.CLASS_NAME, 'ember-text-area')
    textarea.send_keys(str(answer))

    send_button = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission')
    send_button.click()

    message = browser.find_element(By.CSS_SELECTOR, '.smart-hints p').text
    if not message == 'Correct!':
        pytest.xfail(message)
