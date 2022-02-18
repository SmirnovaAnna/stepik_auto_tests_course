import pytest
from selenium import webdriver
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_different_language_find_basket_button(browser):
    """The basket search

    :param: browser: selenium browser object
    
    :return: None
    """
    browser.get(link)
    button = browser.find_elements_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button, "Basket button not found"
   