from selenium.webdriver.common.by import By
from pages.base_page import BasePage


email_field = (By.ID, 'email')
pass_field = (By.ID, 'pass')
send_button = (By.ID, 'send2')
validation_err = (By.XPATH, '//div[@for="email"]')
error_alert = (By.XPATH, '//div[@role="alert"]')


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/customer/account/login'

    def enter_text_into_email(self, text):
        self.find(email_field).send_keys(text)

    def enter_text_into_pass(self, text):
        self.find(pass_field).send_keys(text)

    def click_send_button(self):
        self.find(send_button).click()

    def validation_error_displayed(self):
        return self.find(validation_err).is_displayed()

    def alert_error_displayed(self):
        return self.find(error_alert).text == 'aksdjfaskjf'
