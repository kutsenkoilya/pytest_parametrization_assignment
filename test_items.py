
"""
Run as :
pytest --language=es test_items.py

"""

from selenium.common.exceptions import NoSuchElementException
from locators import ProductPageLocators

def test_product_page_contains_add_button(browser):
    #Open product page
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #validate that element exists
    is_element_exits = False
    try:
        is_element_exits = browser.find_element(*ProductPageLocators.ADD_TO_THE_BASKET_BUTTON)
    except (NoSuchElementException):
        is_element_exits = False
    assert is_element_exits, '<<Add to the Basket>> element doesnt exits'
