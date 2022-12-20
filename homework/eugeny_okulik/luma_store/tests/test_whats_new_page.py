import allure


@allure.feature('Whats new')
@allure.story('products list')
def test_products_count(driver, whats_new):
    assert whats_new.products_count == 4


@allure.feature('Whats new')
@allure.story('Left navigation panel')
def test_no_items_to_compare(driver, whats_new):
    assert whats_new.compare_products_block_text == 'You have no items to compare.'
