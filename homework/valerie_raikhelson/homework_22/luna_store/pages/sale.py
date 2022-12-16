from pages.base_page import BasePage
from pages.locators import sale as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.test_data import data as td
import allure


class SalePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = td.sale_url

    @allure.step('Get title')
    def get_title(self):
        return self.get_text(loc.tittle)

    @allure.step('Click on "shopping cart" icon')
    def click_shopping_cart_icon(self):
        self.click(loc.shopping_cart_icon)

    @allure.step('Get message that the "Shopping cart" is empty')
    def get_empty_shopping_cart_msg(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.empty_shopping_cart_msg))
        return self.get_text(loc.empty_shopping_cart_msg)

    @allure.step('Click on "women deal"')
    def click_shop_women_deal_btn(self):
        self.click(loc.shop_women_deal_btn)
