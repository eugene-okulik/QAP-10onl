from pages.base_page import BasePage
from pages.locators import login_page as loc


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://magento.softwaretestingboard.com/customer/account/login')

    def enter_text_into_email(self, text):
        self.find(loc.email_field).send_keys(text)

    def enter_text_into_pass(self, text):
        self.find(loc.pass_field).send_keys(text)

    def click_send_button(self):
        self.find(loc.send_button).click()

    def validation_error_displayed(self):
        return self.find(loc.validation_err).is_displayed()

    def alert_error_displayed(self):
        return self.find(loc.error_alert).text == 'aksdjfaskjf'
