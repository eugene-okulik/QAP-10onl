from pages.create_account import CreateAccountPage


def test_first_name_is_required(driver):
    create_account = CreateAccountPage(driver)
    create_account.open()
    create_account.click_create_account_btn()
    assert create_account.get_first_name_err() == 'This is a required field.'


def test_email_field_should_contain_at_symbol(driver):
    create_account = CreateAccountPage(driver)
    create_account.open()
    create_account.enter_email('val.dan.com')
    create_account.click_create_account_btn()
    assert create_account.get_email_error().__contains__('Please enter a valid email address')


def test_checkbox_is_selected(driver):
    create_account = CreateAccountPage(driver)
    create_account.open()
    create_account.click_send_newsletter()
    assert create_account.is_news_checkbox_selected()
