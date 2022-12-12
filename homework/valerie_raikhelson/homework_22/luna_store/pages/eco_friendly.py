from time import sleep

from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from pages.locators import eco_friendly as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EcoFriendlyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/collections/eco-friendly.html'

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

    def click_24_items(self):
        self.select_by_value(loc.select_amount_items, '24')

    def products_count(self):
        sleep(3)
        return len(self.find_all(loc.products_list))

    def compare_text(self):
        return self.get_text(loc.empty_items_to_compare)

    def get_email_error(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.email_err))
        return self.get_text(loc.email_err)
