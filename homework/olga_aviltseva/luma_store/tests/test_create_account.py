from pages.create_an_account_page import CreateAnAccount


def test_check_password_not_the_same(driver):
    create_account = CreateAnAccount(driver)
    create_account.open()
    create_account.scroll_page()
    create_account.send_password('Password2022')
    create_account.send_confirm_password('password2022')
    create_account.click_create_account_button()
    create_account.scroll_page()
    assert create_account.compare_password().__contains__('Please enter the same value again.')
