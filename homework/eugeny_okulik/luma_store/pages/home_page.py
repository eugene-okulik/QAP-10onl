from pages.base_page import BasePage
from selenium.webdriver.common.by import By

whats_new_link = (By.ID, 'ui-id-3')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/'
        # self.whats_new_link = self.find(whats_new_link)

    def click_whats_new_link(self):
        self.find(whats_new_link).click()
