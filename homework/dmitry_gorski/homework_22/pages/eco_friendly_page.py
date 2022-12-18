from pages.base_page import BasePage
from pages.locators import eco_friendly_page as loc


class EcoFriendlyPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/collections/eco-friendly.html'

    @property
    def is_open(self):
        return self.find(loc.PAGE_TITLE).text

    def count_of_items(self):
        return len(self.find_all(loc.ITEMS_LIST))

    @property
    def get_price_of_item(self):
        return self.find(loc.ANA_SPORT_ITEM_PRICE).text
