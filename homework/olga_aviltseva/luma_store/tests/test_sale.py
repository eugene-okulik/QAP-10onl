from pages.sale_page import SalePage


def test_no_items_my_wish_list(driver):
    sale = SalePage(driver)
    sale.open()
    assert sale.check_nothing_to_wish_list().text == 'You have no items in your wish list.'
