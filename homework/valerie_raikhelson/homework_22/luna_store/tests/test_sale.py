from tests.test_data import data as td
import allure


@allure.feature('Sale page')
@allure.description('Verify that page opens properly')
def test_is_page_sale_open(driver, sale):
    assert sale.get_title() == td.title_sale
    assert sale.get_current_url() == td.sale_url


@allure.feature('Sale page')
@allure.story('Shopping cart')
@allure.description('Verify that shopping cart is empty')
def test_cart_is_empty(driver, sale):
    sale.click_shopping_cart_icon()
    assert sale.get_empty_shopping_cart_msg() == td.empty_shopping_cart_msg


@allure.feature('Sale page')
@allure.story('Sale categories')
@allure.description('Verify that page opens properly')
def test_is_page_women_deal_open(driver, sale):
    sale.click_shop_women_deal_btn()
    assert sale.get_current_url() == td.women_sale_url
