from pages.base_page import BasePage
from pages.locators import create_new_customer_account_page as locator


class CreateNewCustomerAccount(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/customer/account/create/'

    def page_title(self):
        return self.find(locator.PAGE_TITLE).text == 'Create New Customer Account'

    def check_box(self):
        return self.find(locator.CHECK_BOX)

    def submit_button(self):
        return self.find_and_submit(locator.SUBMIT_BUTTON)

    def firstname_error(self):
        return self.find(locator.FIRSTNAME_FIELD_ERROR)

    def subscribe_button_submit(self):
        return self.find_and_submit(locator.SUBSCRIBE_BUTTON)

    def subscribe_error(self):
        return self.find(locator.EMAIL_ERROR)

    def mail_field(self):
        return self.find(locator.SUBSCRIBE_FIELD)

    def subscribe_button_find(self):
        return self.find(locator.SUBSCRIBE_BUTTON)
