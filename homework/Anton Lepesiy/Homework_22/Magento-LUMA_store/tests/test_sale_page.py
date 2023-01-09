from pages.sale_page import Sale


def test_is_page_opened(driver):
    sale = Sale(driver)
    sale.open()
    assert sale.page_title()


def test_copyright_text_check(driver):
    sale = Sale(driver)
    sale.open()
    assert sale.page_title()


def test_hoodies(driver):
    sale = Sale(driver)
    sale.open()
    assert sale.hoodies()
