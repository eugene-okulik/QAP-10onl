from pytest_bdd import scenario, given, when, then
from pages.login_page import LoginPage
import allure


@allure.feature('Login')
@allure.story('Validation errors')
@scenario('login.feature', 'email field is validated')
def test_login_validation():
    pass


@allure.feature('Login')
@allure.story('Validation errors')
@scenario('login.feature', 'incorrect login alert')
def test_incorrect_login_alert():
    pass


@given('I am on a login page')
def open_login_page(driver):
    LoginPage(driver).open()


@when('I enter abrakadabra into email field')
def enter_abrakadabra_into_email(driver):
    LoginPage(driver).enter_text_into_email('abrakadabra')


@when('I enter valid password')
def enter_valid_password(driver):
    LoginPage(driver).enter_text_into_pass('roni_cost3@example.com')


@when('I click Send button')
def click_send_button(driver):
    LoginPage(driver).click_send_button()


@when('I enter non-existing user email into email field')
def enter_incorrect_email(driver):
    LoginPage(driver).enter_text_into_email('abra@abra.com')


@then('I see validation error')
def validation_error_check(driver):
    assert LoginPage(driver).validation_error_displayed()


@then('I see alert message')
def check_alert_message(driver):
    assert LoginPage(driver).alert_error_displayed()
