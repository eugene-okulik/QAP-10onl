from pages.base_page import BasePage
from pages.locators import eco_friendly_page as locator


class EcoFriendly(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/collections/eco-friendly.html'

    def page_title(self):
        return self.find(locator.PAGE_TITLE).text == 'Eco Friendly'

    def displayed_items(self):
        elements_list = self.find_all(locator.ITEMS)
        return len(elements_list) == 12

    def cart(self):
        return self.find(locator.CART)

