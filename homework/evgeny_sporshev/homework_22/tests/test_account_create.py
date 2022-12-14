from pages.account_create import AccountCreate


def test_is_page_opened(driver):
    account_create = AccountCreate(driver)
    account_create.open()
    assert account_create.is_page_opened()


def test_is_cart_button_shown(driver):
    account_create = AccountCreate(driver)
    account_create.open()
    assert account_create.is_cart_button_shown()


def test_is_first_name_placeholder_shown(driver):
    account_create = AccountCreate(driver)
    account_create.open()
    assert account_create.is_first_name_placeholder_shown()
