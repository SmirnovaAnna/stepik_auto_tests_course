import unittest

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegistration(unittest.TestCase):
   def test_registration2(self):
        """Filling out the form and registering

        The result of the function execution is a completed and submitted form 
        
        :return: None
        """
        LINK = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(LINK)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(
         By.XPATH, '//input[@placeholder="Input your first name"]'
        )
        input1.send_keys("Ivan")
        input2 = browser.find_element(
         By.XPATH, '//input[@placeholder="Input your last name"]'
        )
        input2.send_keys("Petrov")
        input3 = browser.find_element(
         By.XPATH, '//input[@placeholder="Input your email"]'
        )
        input3.send_keys("leningrad@list.ru")
        input4 = browser.find_element(
         By.XPATH, '//input[@placeholder="Input your phone:"]'
        )
        input4.send_keys("8-9567-456-34-56")
        input5 = browser.find_element(
         By.XPATH, '//input[@placeholder="Input your address:"]'
        )
        input5.send_keys("Smolensk")

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
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")



if __name__ == "__main__":
    unittest.main()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()