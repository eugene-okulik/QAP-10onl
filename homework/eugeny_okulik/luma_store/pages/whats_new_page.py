from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import what_new_page as loc


class WhatsNewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/what-is-new.html'
        self.open()

    def open(self):
        self.driver.get(self.page_url)
        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.text_to_be_present_in_element(
                loc.empty_items_to_compare,
                'You have no items to compare.')
        )

    def is_page_opened(self):
        assert self.find(loc.page_title).text == "What's New"
        return self.driver.current_url == self.page_url

    def check_4_products_on_the_page(self):
        return len(self.find_all(loc.products_list)) == 4

    def products_count(self):
        return len(self.find_all(loc.products_list))

    def check_nothing_to_compare(self):
        return self.find(loc.empty_items_to_compare).text == 'You have no items to compare.'

    def compare_text(self):
        return self.find(loc.empty_items_to_compare).text
