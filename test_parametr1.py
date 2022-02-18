import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    """Starts the browser and stops it when the test is over 
    
    :return: None
    """
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    """Search for a link in a given language

    :param: browser: selenium browser object
    
    :return: None
    """
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")