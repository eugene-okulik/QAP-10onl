from pages.sale import Sale


def test_is_page_opened(driver):
    sale = Sale(driver)
    sale.open()
    assert sale.is_page_opened()


def test_is_sale_button_underlined(driver):
    sale = Sale(driver)
    sale.open()
    assert sale.is_sale_button_underlined()


def test_is_navigation_menu_shown(driver):
    sale = Sale(driver)
    sale.open()
    assert sale
