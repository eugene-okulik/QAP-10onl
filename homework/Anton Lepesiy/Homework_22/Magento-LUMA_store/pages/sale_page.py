from pages.base_page import BasePage
from pages.locators import sale_page as locator


class Sale(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/sale.html'

    def page_title(self):
        return self.find(locator.PAGE_TITLE).text == 'Sale'

    def copyright(self):
        return self.find(locator.COPYRIGHT).text == 'Copyright © 2013-present Magento, Inc. All rights reserved.'

    def hoodies(self):
        self.find(locator.HOODIES).click()
        self.driver.implicitly_wait(3)
        return self.find(locator.HOODIES_PAGE_TITLE).text == 'Hoodies & Sweatshirts'
