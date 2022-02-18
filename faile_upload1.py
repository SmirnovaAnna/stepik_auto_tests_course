import time

import os 

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()


# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(1)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/file_input.html")
time.sleep(1)


input1=driver.find_element_by_css_selector('[name="firstname"]')
input1.send_keys("Алиса")

input2 = driver.find_element_by_css_selector('[name="lastname"]')
input2.send_keys("Селезнева")

input3 = driver.find_element_by_css_selector('[name="email"]')
input3.send_keys("alisa@gmail.com")

# получаем путь к директории текущего исполняемого файла 
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, '2_2_8.txt')           
file_button = driver.find_element_by_css_selector('[type="file"]')

file_button.send_keys(file_path)


# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector('[type="submit"]')
driver.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(10)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()

