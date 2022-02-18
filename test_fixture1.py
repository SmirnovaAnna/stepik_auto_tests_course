from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        """Starts the browser through setup_class
    
        :return: None
        """
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        """Stops the browser when the test is over through teardown_class
    
        :return: None
        """
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        """The login link search
    
        :return: None
        """
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        """The basket search
    
        :return: None
        """
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        """Starts the browser through setup_method
    
        :return: None
        """
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        """Stops the browser when the test is over through teardown_method
    
        :return: None
        """
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
