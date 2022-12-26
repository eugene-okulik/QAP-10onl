from pages.base_page import BasePage
from pages.locators import account_page_locators as loc


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/customer/account/create/'

    def is_page_opened(self):
        return self.find(loc.page_title).text == 'Create New Customer Account'

    def is_cart_button_shown(self):
        return self.find(loc.cart_button)

    def is_first_name_placeholder_shown(self):
        return self.find(loc.first_name_placeholder)
