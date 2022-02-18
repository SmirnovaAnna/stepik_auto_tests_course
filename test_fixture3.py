import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    """Starts the browser and stops it when the test is over 
    
    :return: None
    """
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        """The login link search

        :param: browser: selenium browser object
    
        :return: None
        """
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        """The basket search

        :param: browser: selenium browser object
    
        :return: None
        """
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")