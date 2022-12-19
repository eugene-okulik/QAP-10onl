from pages.base_page import BasePage
from pages.locators import create_account_page as loc


class CreateAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/customer/account/create/'

    def is_page_opened(self):
        assert self.find(loc.page_title).text == "Create New Customer Account"
        return self.driver.current_url == self.page_url

    def create_account_button_text(self):
        return self.find(loc.create_account_button).text

    def click_create_account_button(self):
        self.click(loc.create_account_button)

    def is_5_errors_on_empty_form(self):
        return len(self.find_all(loc.validation_errors)) == 5

    def count_errors_on_empty_form(self):
        return len(self.find_all(loc.validation_errors))
