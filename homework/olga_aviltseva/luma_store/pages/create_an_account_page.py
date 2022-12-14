from pages.base_page import BasePage
from pages.locators import create_an_account_page as loc


class CreateAnAccount(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://magento.softwaretestingboard.com/customer/account/create/')

    def find_password_field(self):
        return self.find(loc.password_field)

    def click_password_field(self):
        self.click(loc.password_field)

    def find_confirm_password_field(self):
        return self.find(loc.confirm_password_field)

    def click_confirm_password_field(self):
        self.click(loc.confirm_password_field)

    def send_password(self, password):
        self.send_text(loc.password_field, password)

    def send_confirm_password(self, password):
        self.send_text(loc.confirm_password_field, password)

    def click_create_account_button(self):
        self.click(loc.create_an_account_button)

    def compare_password(self):
        self.find(loc.error_massage)
        return self.get_text(loc.error_massage)
