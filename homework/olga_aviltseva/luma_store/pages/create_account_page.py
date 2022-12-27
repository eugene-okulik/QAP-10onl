from pages.base_page import BasePage
from pages.locators import create_account_page as loc


class CreateAnAccount(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://magento.softwaretestingboard.com/customer/account/create/')

    def send_password(self, text):
        self.send(loc.password_field, text)

    def send_confirm_password(self, text):
        self.send(loc.confirm_password_field, text)

    def click_create_account_button(self):
        self.find(loc.create_account_button).click()

    def click_checkbox_news(self):
        self.find(loc.checkbox_news).click()

    def is_selected_checkbox(self):
        return self.find(loc.checkbox_news).is_selected()

    def get_password_message(self):
        return self.get_text(loc.password_strength_message)
