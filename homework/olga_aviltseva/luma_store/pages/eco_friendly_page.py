from pages.base_page import BasePage
from pages.locators import eco_friendly_page as loc


class EcoFriendlyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://magento.softwaretestingboard.com/collections/eco-friendly.html')

    def count_products_on_the_page(self):
        return len(self.find_all(loc.products_list))

    def click_style_1_filter(self):
        self.find(loc.style_1_filter).click()

    def check_style_1_content(self):
        return self.find(loc.style_1_filter_content).is_displayed()

    def click_base_layer_link(self):
        self.find(loc.base_layer_link).click()
