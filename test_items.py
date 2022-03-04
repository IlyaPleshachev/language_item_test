link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_see_basket(browser):
    browser.get(link)
    #time.sleep(10) #для удобства, просто убери первую решетку
    assert browser.find_element_by_css_selector("#add_to_basket_form > button")