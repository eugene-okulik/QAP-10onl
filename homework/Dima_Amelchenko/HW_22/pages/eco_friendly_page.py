from pages.base_page import BasePage
from pages.locators import locators_eco_friendly_page as locator_2
from selenium.webdriver.support.ui import Select


class EcoFriendly(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://magento.softwaretestingboard.com/collections/eco-friendly.html')

    def check_title(self):
        return self.find(locator_2.eco_friendly_title).text

    def check_url(self):
        return self.driver.current_url

    def check_price_first_product(self):
        return self.find(locator_2.price_first_product).text
