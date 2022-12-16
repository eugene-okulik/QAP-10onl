from pages.base_page import BasePage
from pages.locators import create_acount as loc
from tests.test_data import data as td
import allure


class CreateAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = td.create_acc_url

    @allure.step('Click on "Create account"')
    def click_create_account_btn(self):
        self.click(loc.create_account_btn)

    @allure.step('Get first name error')
    def get_first_name_err(self):
        return self.get_text(loc.first_name_err)

    @allure.step('Enter email')
    def enter_email(self, email):
        self.set_text(loc.email_field, email)

    @allure.step('Get email error')
    def get_email_error(self):
        return self.get_text(loc.email_err)

    @allure.step('Mark news checkbox')
    def click_send_newsletter(self):
        self.click(loc.news_checkbox)

    @allure.step('Verify that news  checkbox is selected')
    @allure.id
    def is_news_checkbox_selected(self):
        return self.is_selected(loc.news_checkbox)
