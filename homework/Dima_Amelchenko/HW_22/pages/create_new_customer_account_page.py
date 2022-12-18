from pages.base_page import BasePage
from pages.locators import locators_reate_new_customer_account as locator_1


class CreateNewCustomerAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://magento.softwaretestingboard.com/customer/account/create/')

    def filling_out_form(self):
        self.find(locator_1.first_name).send_keys('Kazimir')
        self.find(locator_1.last_name).send_keys('Malevich')
        self.find(locator_1.email).send_keys('malevichkazimir233@gmail.com')
        self.find(locator_1.password).send_keys('123456789Kazimir+')
        self.find(locator_1.confirm_password).send_keys('123456789Kazimir+')
        self.find(locator_1.create_an_account_button).click()

    def check_my_account(self):
        return self.find(locator_1.my_account).text
