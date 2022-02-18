from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

path=GeckoDriverManager().install()
browser = webdriver.Firefox(executable_path=path)
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element_by_id("submit")