import allure
from pages.base_page import BasePage
from pages.locators import eco_friendly as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.test_data import data as td


class EcoFriendlyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = td.eco_friendly_url

    def open(self):
        self.driver.get(self.page_url)
        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.text_to_be_present_in_element(
                loc.empty_items_to_compare, td.no_items_msg)
        )

    @allure.step('Click on 24 in select box')
    def click_24_items(self):
        self.select_by_value(loc.select_amount_items, '24')

    @allure.step('Count the number of products')
    def products_count(self, length):
        WebDriverWait(self.driver, 20).until(
            lambda browser: len(self.find_all(loc.products_list)) == int(length))
        return len(self.find_all(loc.products_list))

    @allure.step('Get message that there are no products to compare')
    def compare_text(self):
        return self.get_text(loc.empty_items_to_compare)

    @allure.step('Get email error')
    def get_email_error(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.email_err))
        return self.get_text(loc.email_err)
