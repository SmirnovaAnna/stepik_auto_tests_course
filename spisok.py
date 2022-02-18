import time
from selenium.webdriver.support.ui import Select
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()


# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(1)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/selects1.html")
time.sleep(1)

x=driver.find_element_by_id("num1").text
y = driver.find_element_by_id("num2").text

z=int(x)+int(y)
print(z)

str(z)
print(z)

z_element=driver.find_element_by_tag_name("select").click()
z_element=driver.find_element_by_css_selector(f"[value='{z}']").click()

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector('[type="submit"]')

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(10)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()

