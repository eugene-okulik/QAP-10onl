from pages.account_page import AccountPage
import allure


@allure.feature('Account page')
@allure.story('Page open')
def test_is_page_opened(driver):
    with allure.step('Open account page'):
        account_page = AccountPage(driver)
        account_page.open()
    assert account_page.is_page_opened()


@allure.feature('Account page')
@allure.story('Cart button shown')
def test_is_cart_button_shown(driver):
    with allure.step('button shown'):
        account_page = AccountPage(driver)
        account_page.open()
    assert account_page.is_cart_button_shown()


def test_is_first_name_placeholder_shown(driver):
    account_page = AccountPage(driver)
    account_page.open()
    assert account_page.is_first_name_placeholder_shown()
