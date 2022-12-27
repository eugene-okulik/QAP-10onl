from pages.create_account_page import CreateAnAccount
from time import sleep


def test_check_checkbox_is_selected(driver):
    create_account = CreateAnAccount(driver)
    create_account.open()
    create_account.click_checkbox_news()
    assert create_account.is_selected_checkbox()


def test_massage_no_password(driver):
    create_account = CreateAnAccount(driver)
    create_account.open()
    assert create_account.get_password_message() == 'No Password'


def test_massage_strong_password(driver):
    create_account = CreateAnAccount(driver)
    create_account.open()
    create_account.scroll_page()
    create_account.send_password('Password2022')
    sleep(3)  # Оставила специально, не забыла убрать
    create_account.click_create_account_button()
    assert create_account.get_password_message() == 'Very Strong'
