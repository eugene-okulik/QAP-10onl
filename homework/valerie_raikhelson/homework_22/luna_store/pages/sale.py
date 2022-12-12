from pages.base_page import BasePage
from pages.locators import sale as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SalePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/sale.html'

    def get_title(self):
        return self.get_text(loc.tittle)

    def click_shopping_cart_icon(self):
        self.click(loc.shopping_cart_icon)

    def get_empty_shopping_cart_msg(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.empty_shopping_cart_msg))
        return self.get_text(loc.empty_shopping_cart_msg)

    def click_shop_women_deal_btn(self):
        self.click(loc.shop_women_deal_btn)
