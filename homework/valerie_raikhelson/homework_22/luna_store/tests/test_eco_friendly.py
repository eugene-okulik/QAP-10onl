from tests.test_data import data as td
import allure


@allure.feature('Eco-friendly page')
@allure.story('Products list')
@allure.description('Verify that 12 products are displayed')
def test_max_12_items_are_displayed_on_the_page(driver, eco_friendly):
    assert eco_friendly.products_count(12) == 12


@allure.feature('Eco-friendly page')
@allure.story('Products list')
@allure.description('Verify that 18 products are displayed')
def test_max_24_items_are_displayed_on_the_page(driver, eco_friendly):
    eco_friendly.click_24_items()
    assert eco_friendly.products_count(18) == 18


@allure.feature('Eco-friendly page')
@allure.story('Left navigation panel')
@allure.description('Verify that message is displayed in case when products for comparison are not selected')
def test_no_items_to_compare(driver, eco_friendly):
    assert eco_friendly.compare_text() == td.no_items_msg
