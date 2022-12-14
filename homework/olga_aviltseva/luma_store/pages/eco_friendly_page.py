from pages.base_page import BasePage
from pages.locators import eco_friendly_page as loc


class EcoFriendlyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://magento.softwaretestingboard.com/collections/eco-friendly.html')

    def check_12_products_on_the_page(self):
        return len(self.find_all(loc.products_list))
