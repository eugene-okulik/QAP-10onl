from pages.base_page import BasePage
from pages.locators import loc_create_page as loc


class CreatePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/customer/account/create/'

    def get_element_text(self):
        element = self.find(loc.title_text)
        return element.text

    def element_is_displayed(self):
        return self.find(loc.create_account_button).is_displayed()

    def count_displayed_elements(self):
        return len(self.find_all(loc.required_fields))

    def click_element(self):
        element = self.find(loc.create_account_button)
        element.click()
