from pages.sale_page import SalePage


def test_sale_page_link(driver):
    sale = SalePage(driver)
    sale.open()
    assert sale.check_title_page() == 'Sale'


def test_no_items_my_wish_list(driver):
    sale = SalePage(driver)
    sale.open()
    assert sale.check_nothing_to_wish_list().text == 'You have no items in your wish list.'


def test_shop_womens_deals_button(driver):
    sale = SalePage(driver)
    sale.open()
    assert sale.is_shop_womens_deals_button_present()
