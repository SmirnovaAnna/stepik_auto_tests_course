import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()


# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(1)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/explicit_wait2.html")



button = WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
# Найдем кнопку, которая отправляет введенное решение
button = driver.find_element_by_id("book")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()


x_element = driver.find_element_by_css_selector('[id="input_value"]')
x = x_element.text
print(x)
y = calc(x)
print(y)
input=driver.find_element_by_css_selector('[id="answer"]')
input.send_keys(y)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector('[type="submit"]')

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()

time.sleep(50)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()

