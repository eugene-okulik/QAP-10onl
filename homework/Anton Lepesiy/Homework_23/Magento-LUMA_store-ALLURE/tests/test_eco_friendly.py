from pages.eco_friendly_page import EcoFriendly
import allure


@allure.feature('ECO-Friendly page')
@allure.story('Page is open correctly')
def test_is_page_opened(driver):
    with allure.step('Open page'):
        eco_friendly = EcoFriendly(driver)
        eco_friendly.open()
    with allure.step('Page is open'):
        assert eco_friendly.page_title()


@allure.feature('ECO-Friendly page')
@allure.story('displayed elements')
def test_cart_showed(driver):
    with allure.step('Open page'):
        eco_friendly = EcoFriendly(driver)
        eco_friendly.open()
    with allure.step('check element visibility'):
        assert eco_friendly.cart().is_displayed()


@allure.feature('ECO-Friendly page')
@allure.story('displayed elements')
def test_items_count(driver):
    with allure.step('Open page'):
        eco_friendly = EcoFriendly(driver)
        eco_friendly.open()
    with allure.step('check elements visibility'):
        assert eco_friendly.displayed_items()
