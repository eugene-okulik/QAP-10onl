from pages.base_page import BasePage
from pages.locators import eco_friendly_page as loc


class EcoFriendlyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/collections/eco-friendly.html'

    def is_page_opened(self):
        assert self.find(loc.page_title).text == "Eco Friendly"
        return self.driver.current_url == self.page_url

    def is_12_products_on_the_page(self):
        return len(self.find_all(loc.products_list)) == 12

    def products_count(self):
        return len(self.find_all(loc.products_list))

    def is_12_with_lists_on_the_page(self):
        return len(self.find_all(loc.add_to_with_list)) == 12

    def wish_lists_count(self):
        return len(self.find_all(loc.add_to_with_list))
