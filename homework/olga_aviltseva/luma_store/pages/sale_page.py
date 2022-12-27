from pages.base_page import BasePage
from pages.locators import sale_page as loc


class SalePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://magento.softwaretestingboard.com/sale.html')

    def check_nothing_to_wish_list(self):
        return self.find(loc.empty_items_to_wish_list)

    def check_title_page(self):
        return self.find(loc.page_title).text

    def is_shop_womens_deals_button_present(self):
        return self.find(loc.shop_womens_deals_button).is_displayed()
