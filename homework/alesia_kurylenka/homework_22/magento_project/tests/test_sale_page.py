from pages.sale_page import SalePage


def test_sale_link(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    assert sale_page.page_url == 'https://magento.softwaretestingboard.com/sale.html'


def test_shop_women_deals_button_text(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    assert sale_page.shop_women_deals_button_text() == 'Shop Women’s Deals'


def test_is_present_gear_deals_menu(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    sale_page.page_zoom("document.body.style.zoom = '0.5'")
    assert sale_page.check_gear_deals_text() == "GEAR DEALS"
