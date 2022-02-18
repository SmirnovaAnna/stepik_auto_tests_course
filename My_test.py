from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    path=GeckoDriverManager().install()
    browser = webdriver.Firefox(executable_path=path)
    browser.get(link)


    name = browser.find_element_by_tag_name('input')
    name.click()
    name.send_keys("Artur")


    em = browser.find_element_by_tag_name('input')
    em.click()
    em.send_keys('ara@gmail.com')

    ph = browser.find_element_by_xpath('/html/body/div/form/div[2]/div[1]/input')
    ph.click()
    ph.send_keys('+998900000000')

    ad = browser.find_element_by_xpath('/html/body/div/form/div[2]/div[2]/input')
    ad.click()
    ad.send_keys('Yun Ab')
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(10)

    browser.quit()

