from pages.sale_page import Sale


def test_message(driver):
    sale = Sale(driver)
    sale.open()
    assert sale.check_title() == 'Pristine prices on pants, tanks and bras.'


def test_check_men_s_bargains(driver):
    sale = Sale(driver)
    assert sale.check_men_s_bargains() == "Men’s Bargains"


def test_check_luma_gear_steals(driver):
    sale = Sale(driver)
    assert sale.check_luma_gear_steals() == "Luma Gear Steals"
