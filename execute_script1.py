import time

import math

def calc(x):
  """Calculates using the formula 

  :param: x

  :return: formula value in string format 
  """
  return str(math.log(abs(12*math.sin(int(x)))))

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()


# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(1)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://SunInJuly.github.io/execute_script.html")
time.sleep(1)

x=driver.find_element_by_id("input_value").text
y=calc(x)


input=driver.find_element_by_css_selector('[id="answer"]')
input.send_keys(y)

option1 = driver.find_element_by_css_selector('[id="robotCheckbox"]')
option1.click()

option2 = driver.find_element_by_css_selector('[id="robotsRule"]')
option2.click()


# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector('[type="submit"]')
driver.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(10)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()

