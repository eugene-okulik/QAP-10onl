from pages.account_page import AccountPage


def test_is_page_opened(driver):
    account_page = AccountPage(driver)
    account_page.open()
    assert account_page.is_page_opened()


def test_is_cart_button_shown(driver):
    account_page = AccountPage(driver)
    account_page.open()
    assert account_page.is_cart_button_shown()


def test_is_first_name_placeholder_shown(driver):
    account_page = AccountPage(driver)
    account_page.open()
    assert account_page.is_first_name_placeholder_shown()
