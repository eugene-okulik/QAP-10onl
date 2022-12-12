from pages.base_page import BasePage
from pages.locators import create_acount as loc


class CreateAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/customer/account/create/'

    def click_create_account_btn(self):
        self.click(loc.create_account_btn)

    def get_first_name_err(self):
        return self.get_text(loc.first_name_err)

    def enter_email(self, email):
        self.set_text(loc.email_field, email)

    def get_email_error(self):
        return self.get_text(loc.email_err)

    def click_send_newsletter(self):
        self.click(loc.news_checkbox)

    def is_news_checkbox_selected(self):
        return self.is_selected(loc.news_checkbox)
