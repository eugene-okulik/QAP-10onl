import pytest
from pages.create_account_page import CreateAccountPage


@pytest.mark.smoke
def test_page_is_open(driver):
    account_page = CreateAccountPage(driver)
    account_page.open()
    assert account_page.is_open == 'Create New Customer Account'


@pytest.mark.simple
def test_subscribe_box(driver):
    account_page = CreateAccountPage(driver)
    account_page.open()
    account_page.click_to_elem()
    assert account_page.check_if_activate()


@pytest.mark.hard
def test_created_customer(driver):
    account_page = CreateAccountPage(driver)
    account_page.open()
    account_page.check_account_form(firstname='testQQAP10',
                                    lastname='testQQAP10',
                                    email='testQQAP10@testQQAP10.com',
                                    password='vmQwS{e~@QWE')
