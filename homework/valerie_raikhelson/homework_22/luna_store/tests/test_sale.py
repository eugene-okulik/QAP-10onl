from pages.sale import SalePage


def test_is_page_sale_open(driver):
    sale = SalePage(driver)
    sale.open()
    assert sale.get_title() == "Sale"
    assert sale.get_current_url() == 'https://magento.softwaretestingboard.com/sale.html'


def test_cart_is_empty(driver):
    sale = SalePage(driver)
    sale.open()
    sale.click_shopping_cart_icon()
    assert sale.get_empty_shopping_cart_msg() == 'You have no items in your shopping cart.'


def test_is_page_women_deal_open(driver):
    sale = SalePage(driver)
    sale.open()
    sale.click_shop_women_deal_btn()
    assert sale.get_current_url() == 'https://magento.softwaretestingboard.com/promotions/women-sale.html'
