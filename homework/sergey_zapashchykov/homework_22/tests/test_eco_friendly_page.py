from pages.eco_friendly_page import EcoFriendlyPage


def test_get_title_text(driver):
    eco_friendly_page = EcoFriendlyPage(driver)
    eco_friendly_page.open()
    assert eco_friendly_page.get_element_text() == 'Eco Friendly'


def test_products_is_displayed_12(driver):
    products = EcoFriendlyPage(driver)
    products.open()
    products.scroll_down()
    assert products.count_displayed_elements() == 12


def test_my_cart_is_displayed(driver):
    my_cart = EcoFriendlyPage(driver)
    my_cart.open()
    assert my_cart.element_is_displayed()
