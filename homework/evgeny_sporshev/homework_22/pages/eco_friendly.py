from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as locator
import time


class EcoFriendly(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/collections/eco-friendly.html'

    def is_page_opened(self):
        return self.find(locator.page_title).text == 'Eco Friendly'

    def is_search_placeholder_shown(self):
        return self.find(locator.search_placeholder)

    def is_search_suggest_shown(self):
        search_suggest = self.find(locator.search_placeholder)
        search_suggest.send_keys('an')
        time.sleep(1)  # иначе не получается - саджест не выходит :)
        search_suggest.send_keys('a')
        return self.find(locator.search_suggest)
