from pages.sale_page import Sale
import allure


@allure.feature('Sale')
@allure.story('Check massage')
def test_message(driver):
    sale = Sale(driver)
    sale.open()
    assert sale.check_title() == 'Pristine prices on pants, tanks and bras.'
