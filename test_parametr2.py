import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

LINKS = [
    'https://stepik.org/lesson/236895/step/1', 
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
]

text_storage = []
answer = math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    """Starts the browser and stops it when the test is over 
    
    :return: None
    """
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # browser.implicitly_wait
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('links', LINKS)
def test_guest_should_see_login_link(browser, links):
    """Gathers pieces of messages from functional feedback together 

    :param: browser: selenium browser object, links

    :return: None
    """
    link = f"{links}/"
    browser.get(link)

    browser.implicitly_wait(15)

    # найти textarea
    element = browser.find_element_by_css_selector(".textarea")

    # записать в него
    element.send_keys(str(math.log(int(time.time()))))
    # найти кнопку
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    button.click()
    # найти класс сообщения и текст его присвоить переменной
    message_text = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    if message_text != "Correct!":
        text_storage.append(message_text)
        print("\n******* part answer: ", message_text, "*******")


def test_output_answer():
    """Outputs the answer 

    :return: None
    """
    print("\n******* answer: ", "".join(text_storage), "*******")
