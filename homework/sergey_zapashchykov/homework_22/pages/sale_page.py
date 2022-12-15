from pages.base_page import BasePage
from pages.locators import loc_sale_page as loc


class SalePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/sale.html'

    def get_element_text(self):
        element = self.find(loc.title_text)
        return element.text

    def element_is_displayed(self):
        return self.find(loc.subscribe).is_displayed()

    def count_displayed_elements(self):
        return len(self.find_all(loc.content_blocks))
