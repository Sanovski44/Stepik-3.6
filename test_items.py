link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
import time

def test_search_button_basket(browser):
    browser.get(link)
    time.sleep(1)
    x = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert
