from pages.base_page import BasePage
from pages.locators import loc_eco_friendly_page as loc


class EcoFriendlyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/collections/eco-friendly.html'

    def get_element_text(self):
        element = self.find(loc.title_text)
        return element.text

    def element_is_displayed(self):
        return self.find(loc.my_cart).is_displayed()

    def count_displayed_elements(self):
        return len(self.find_all(loc.products))
