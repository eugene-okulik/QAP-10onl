from pages.sale_page import SalePage


def test_sale_link(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    assert sale_page.page_url == 'https://magento.softwaretestingboard.com/sale.html'


def test_is_present_shop_women_deals_button_button(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    assert sale_page.is_present_shop_women_deals_button() == 'Shop Women’s Deals'


def test_is_present_gear_deals_menu(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    sale_page.zoom_out_by_two()
    assert sale_page.gear_deals_menu_text() == "GEAR DEALS"
