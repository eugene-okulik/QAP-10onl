from pytest_bdd import scenario, given, when, then
from pages.login import LoginPage
import allure


@allure.feature('Login')
@allure.story('Validation errors')
@scenario('login.feature', 'email field is validated')
def test_login_validation():
    pass


@given('I am on a login page')
def open_page(driver):
    LoginPage(driver).open()


@when('I enter "aaa" into email field')
def enter_invalid_email(driver):
    LoginPage(driver).enter_email('aaa')


@when('I enter valid password')
def enter_valid_password(driver):
    LoginPage(driver).enter_password('roni_cost3@example.com')


@when('I click Send button')
def click_send_btn(driver):
    LoginPage(driver).click_send_btn()


@then('I see validation error')
def get_validation_err(driver):
    LoginPage(driver).get_validation_err()
