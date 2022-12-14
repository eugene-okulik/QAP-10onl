from pages.create_new_customer_account_page import CreateNewCustomerAccountPage


def test_create_new_account(driver):
    account = CreateNewCustomerAccountPage(driver)
    account.open()
    account.filling_out_form()
    assert account.check_my_account() == 'My Account'
