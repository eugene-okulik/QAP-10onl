from pages.create_new_customer_account_page import CreateNewCustomerAccount


def test_is_page_opened(driver):
    account_creating = CreateNewCustomerAccount(driver)
    account_creating.open()
    assert account_creating.page_title()


def test_check_box(driver):
    account_creating = CreateNewCustomerAccount(driver)
    account_creating.open()
    account_creating.check_box().click()
    assert account_creating.check_box().is_selected()


def test_firstname_error(driver):
    account_creating = CreateNewCustomerAccount(driver)
    account_creating.open()
    driver.implicitly_wait(3)
    account_creating.submit_button()
    assert account_creating.firstname_error().is_displayed()


def test_subscribe_mail_error(driver):
    account_creating = CreateNewCustomerAccount(driver)
    account_creating.open()
    account_creating.mail_field().send_keys('asdfasdf')
    account_creating.subscribe_button_submit()
    assert account_creating.subscribe_error().is_displayed()


def test_subscribe_button_is_displ(driver):
    account_creating = CreateNewCustomerAccount(driver)
    account_creating.open()
    assert account_creating.subscribe_button_find().is_displayed()
