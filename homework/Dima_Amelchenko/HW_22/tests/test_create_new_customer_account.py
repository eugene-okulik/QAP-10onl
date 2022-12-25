from pages.create_new_customer_account_page import CreateNewCustomerAccountPage


def test_create_new_account(driver):
    account = CreateNewCustomerAccountPage(driver)
    account.open()
    account.filling_out_form()
    assert account.check_my_account() == 'My Account'


def test_compare_products(driver):
    account = CreateNewCustomerAccountPage(driver)
    assert account.check_compare_products() == 'Compare Products'


def test_contact_information(driver):
    account = CreateNewCustomerAccountPage(driver)
    assert account.check_contact_information() == 'Contact Information'
