from pages.base_page import BasePage
from pages.locators import sale_page as loc


class SalePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/sale.html'

    def is_page_opened(self):
        assert self.find(loc.page_title).text == "Sale"
        return self.driver.current_url == self.page_url

    def is_present_shop_women_deals_button(self):
        return self.find(loc.shop_women_deals).text

    def gear_deals_menu(self):
        return self.find(loc.gear_deals_menu).text == "GEAR DEALS"

    def gear_deals_menu_text(self):
        return self.find(loc.gear_deals_menu).text
