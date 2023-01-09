from pages.create_account_page import CreateAnAccount
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import allure


@allure.feature('Create Account')
@allure.story('Create account form')
def test_check_checkbox_is_selected(driver):
    with allure.step('Open Create Account page'):
        create_account = CreateAnAccount(driver)
        create_account.open()
    with allure.step('Click checkbox'):
        create_account.click_checkbox_news()
    with allure.step('Check checkbox is selected'):
        assert create_account.is_selected_checkbox()


@allure.feature('Create Account')
@allure.story('Create account form')
def test_message_no_password(driver):
    with allure.step('Open Create Account page'):
        create_account = CreateAnAccount(driver)
        create_account.open()
    with allure.step('Check password message'):
        assert create_account.get_password_message() == 'No Password'


@allure.feature('Create Account')
@allure.story('Create account form')
def test_massage_strong_password(driver):
    with allure.step('Open Create Account page'):
        create_account = CreateAnAccount(driver)
        create_account.open()
    with allure.step('Scroll page'):
        create_account.scroll_page()
    with allure.step('Enter password'):
        WebDriverWait(driver, 10).until(ec.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'Default welcome msg!'))
        create_account.send_password('Password2022')
        assert create_account.get_password_message() == 'Very Strong'
