from pages.base_page import BasePage
from pages.locators import locators_sale_page as locator_3


class SalePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://magento.softwaretestingboard.com/sale.html')

    def check_title(self):
        return self.find(locator_3.sale_title).text

    def check_men_s_bargains(self):
        return self.find(locator_3.men_s_bargains).text

    def check_luma_gear_steals(self):
        return self.find(locator_3.luma_gear_steals).text
