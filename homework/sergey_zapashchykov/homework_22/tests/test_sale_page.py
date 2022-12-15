from pages.sale_page import SalePage


def test_get_title_text(driver):
    eco_friendly_page = SalePage(driver)
    eco_friendly_page.open()
    assert eco_friendly_page.get_element_text() == 'Sale'


def test_content_blocks_is_displayed_9(driver):
    products = SalePage(driver)
    products.open()
    products.scroll_down()
    assert products.count_displayed_elements() == 9


def test_my_cart_is_displayed(driver):
    subscribe = SalePage(driver)
    subscribe.open()
    assert subscribe.element_is_displayed()
