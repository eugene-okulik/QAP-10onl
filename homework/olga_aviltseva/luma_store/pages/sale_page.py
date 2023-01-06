from pages.base_page import BasePage
from pages.locators import sale_page as loc


class SalePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://magento.softwaretestingboard.com/sale.html')

    def check_nothing_to_wish_list(self):
        return self.find(loc.empty_items_to_wish_list)

    def page_title_text(self):
        return self.get_text(loc.page_title)

    def is_shop_womens_deals_button_present(self):
        return self.find(loc.shop_womens_deals_button).is_displayed()
