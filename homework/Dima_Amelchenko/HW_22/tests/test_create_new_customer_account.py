from pages.create_new_customer_account_page import CreateNewCustomerAccountPage
import allure


@allure.feature('Create new customer account')
@allure.story('Check account creation')
def test_create_new_account(driver):
    account = CreateNewCustomerAccountPage(driver)
    account.open()
    account.filling_out_form()
    assert account.check_my_account() == 'My Account'
