from pages.base_page import BasePage
from pages.locators import sale_locators as loc


class Sale(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/sale.html'

    def is_page_opened(self):
        return self.find(loc.page_title).text == 'Sale'

    def is_navigation_menu_shown(self):
        return self.find(loc.navigation_menu)

    def is_sale_button_underlined(self):
        return self.find(loc.sale_button_underlined).value_of_css_property('border-color') == 'rgb(255, 85, 1)'
