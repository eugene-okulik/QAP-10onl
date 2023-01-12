from pages.sale_page import Sale
import allure


@allure.feature('Sale page')
@allure.story('Page is open correctly')
def test_is_page_opened(driver):
    with allure.step('Open page'):
        sale = Sale(driver)
        sale.open()
    with allure.step('Page is open'):
        assert sale.page_title()


@allure.feature('Sale page')
@allure.story('displayed elements')
def test_copyright_text_check(driver):
    with allure.step('Open page'):
        sale = Sale(driver)
        sale.open()
    with allure.step('Title check'):
        assert sale.page_title()


@allure.feature('Sale page')
@allure.story('displayed elements')
def test_hoodies(driver):
    with allure.step('Open page'):
        sale = Sale(driver)
        sale.open()
    with allure.step('check elements visibility'):
        assert sale.hoodies()
