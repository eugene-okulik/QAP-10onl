from pages.base_page import BasePage
from selenium.webdriver.common.by import By

sale_title = (By.CLASS_NAME, 'title')


class Sale(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://magento.softwaretestingboard.com/sale.html')

    def check_title(self):
        return self.find(sale_title).text
