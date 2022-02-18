from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

LINK = "http://suninjuly.github.io/simple_form_find_task.html"

is_wait = False
path=GeckoDriverManager().install()
browser = webdriver.Firefox(executable_path=path)
browser.get(LINK)
button = browser.find_element(By.ID, "submit_button")
button.click()

if is_wait == True:
    print("wait 10")
    sleep(10)  
else:
     print("no wait")

# закрываем браузер после всех манипуляций
browser.quit()