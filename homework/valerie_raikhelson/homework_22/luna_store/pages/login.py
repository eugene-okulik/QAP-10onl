from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.test_data import data as td

email_field = (By.CSS_SELECTOR, '#email')
pass_field = (By.CSS_SELECTOR, '#pass')
send_btn = (By.CSS_SELECTOR, '#send2')
validation_err = (By.CSS_SELECTOR, '.message-error.error.message')


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = td.login_url

    def enter_email(self, text):
        self.set_text(email_field, text)

    def enter_password(self, text):
        self.set_text(pass_field, text)

    def click_send_btn(self):
        self.click(send_btn)

    def get_validation_err(self):
        return self.get_text(validation_err)
