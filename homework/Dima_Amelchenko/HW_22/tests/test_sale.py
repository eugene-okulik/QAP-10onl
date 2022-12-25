from pages.sale_page import SalePage


def test_message(driver):
    sale = SalePage(driver)
    sale.open()
    assert sale.check_title() == 'Pristine prices on pants, tanks and bras.'


def test_check_men_s_bargains(driver):
    sale = SalePage(driver)
    assert sale.check_men_s_bargains() == "Men’s Bargains"


def test_check_luma_gear_steals(driver):
    sale = SalePage(driver)
    assert sale.check_luma_gear_steals() == "Luma Gear Steals"
