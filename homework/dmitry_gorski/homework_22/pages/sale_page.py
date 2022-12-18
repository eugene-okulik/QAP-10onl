from pages.base_page import BasePage
from pages.locators import sale_page as loc
from selenium.webdriver.support.color import Color


class SalePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/sale.html'

    @property
    def is_open(self):
        return self.find(loc.PAGE_TITLE).text

    def click_to_elem(self):
        return self.click(loc.JACKET_LINK)

    def count_of_items(self):
        return self.find_all(loc.ITEMS_LIST)

    @property
    def get_color(self):
        free_sales_elem = self.find(loc.FREE_SALES).value_of_css_property('background-color')
        color = Color.from_string(free_sales_elem).hex
        return color
