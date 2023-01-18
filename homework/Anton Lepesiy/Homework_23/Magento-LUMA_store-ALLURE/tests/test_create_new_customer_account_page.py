from pages.create_new_customer_account_page import CreateNewCustomerAccount
import allure


@allure.feature('New Customer page')
@allure.story('Page is open correctly')
def test_is_page_opened(driver):
    with allure.step('Open page'):
        account_creating = CreateNewCustomerAccount(driver)
        account_creating.open()
    with allure.step('Page is open'):
        assert account_creating.page_title()


@allure.feature('New Customer page')
@allure.story('clickable elements')
def test_check_box(driver):
    with allure.step('Open page'):
        account_creating = CreateNewCustomerAccount(driver)
        account_creating.open()
    with allure.step('Click element'):
        account_creating.check_box().click()
    with allure.step('Check element status'):
        assert account_creating.check_box().is_selected()


@allure.feature('New Customer page')
@allure.story('Validation errors')
def test_firstname_error(driver):
    with allure.step('Open page'):
        account_creating = CreateNewCustomerAccount(driver)
        account_creating.open()
    driver.implicitly_wait(3)
    with allure.step('searching element...'):
        account_creating.submit_button()
    with allure.step('check element visibility'):
        assert account_creating.firstname_error().is_displayed()


@allure.feature('New Customer page')
@allure.story('Validation errors')
def test_subscribe_mail_error(driver):
    with allure.step('Open page'):
        account_creating = CreateNewCustomerAccount(driver)
        account_creating.open()
    with allure.step('inputting text'):
        account_creating.mail_field().send_keys('asdfasdf')
    with allure.step('submit input'):
        account_creating.subscribe_button_submit()
    with allure.step('error visibility check'):
        assert account_creating.subscribe_error().is_displayed()


@allure.feature('New Customer page')
@allure.story('clickable elements')
def test_subscribe_button_is_displayed(driver):
    with allure.step('Open page'):
        account_creating = CreateNewCustomerAccount(driver)
        account_creating.open()
    with allure.step('Visibility check'):
        assert account_creating.subscribe_button_find().is_displayed()
