from pages.create_account_page import CreateAccountPage


def test_account_link(driver):
    create_account_page = CreateAccountPage(driver)
    create_account_page.open()
    assert create_account_page.page_url == 'https://magento.softwaretestingboard.com/customer/account/create/'


def test_create_account_button_text(driver):
    create_account_page = CreateAccountPage(driver)
    create_account_page.open()
    create_account_page.scroll_to_bottom()
    assert create_account_page.create_account_button_text() == 'Create an Account'


def test_validations_errors_on_empty_form(driver):
    create_account_page = CreateAccountPage(driver)
    create_account_page.open()
    create_account_page.scroll_to_bottom()
    create_account_page.click_create_account_button()
    create_account_page.page_zoom("document.body.style.zoom = '0.5'")
    assert create_account_page.count_errors_on_empty_form() == 5
