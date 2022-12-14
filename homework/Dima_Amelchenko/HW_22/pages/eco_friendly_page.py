from pages.base_page import BasePage
from selenium.webdriver.common.by import By

eco_friendly_title = (By.CLASS_NAME, 'page-title-wrapper')


class EcoFriendly(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://magento.softwaretestingboard.com/collections/eco-friendly.html')

    def check_title(self):
        return self.find(eco_friendly_title).text
