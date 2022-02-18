from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

try: 
    #LINK = "http://suninjuly.github.io/registration1.html"
    LINK = "http://suninjuly.github.io/registration2.html"
    path=GeckoDriverManager().install()
    browser = webdriver.Firefox(executable_path=path)
    browser.get(LINK)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
    input3.send_keys("leningrad@list.ru")
    input4 = browser.find_element(By.XPATH, '//input[@placeholder="Input your phone:"]')
    input4.send_keys("8-9567-456-34-56")
    input5 = browser.find_element(By.XPATH, '//input[@placeholder="Input your address:"]')
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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()