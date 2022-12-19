from tests.test_data import data as td
import allure


@allure.feature('Create account page')
@allure.story('Validation errors')
@allure.description('Verify that first name field is required')
def test_first_name_is_required(driver, create_account):
    create_account.click_create_account_btn()
    assert create_account.get_first_name_err() == td.first_name_err


@allure.feature('Create account page')
@allure.story('Validation errors')
@allure.description('Verify that email should contain @ symbol')
def test_email_field_should_contain_at_symbol(driver, create_account):
    create_account.enter_email(td.email)
    create_account.click_create_account_btn()
    assert create_account.get_email_error().__contains__(td.email_err)


@allure.feature('Create account page')
@allure.story('Create account form')
@allure.description('Verify that new letter checkbox has been selected')
def test_checkbox_is_selected(driver, create_account):
    create_account.click_send_newsletter()
    assert create_account.is_news_checkbox_selected()
