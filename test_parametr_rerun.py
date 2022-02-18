link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    """The login link search

    :param: browser: selenium browser object
    
    :return: None
    """
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    """The magic link search

    :param: browser: selenium browser object
    
    :return: None
    """
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")