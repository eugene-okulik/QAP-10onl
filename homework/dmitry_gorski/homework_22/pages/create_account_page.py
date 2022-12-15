from pages.base_page import BasePage
from pages.locators import account_page as loc


class CreateAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/customer/account/create/'
        self.form_list = list()

    @property
    def is_open(self):
        return self.find(loc.PAGE_TITLE).text

    def click_to_elem(self):
        return self.click(loc.SUBSCRIBE_CHECKBOX)

    def check_if_activate(self):
        return self.find(loc.SUBSCRIBE_CHECKBOX).is_selected()

    def check_account_form(self, **kwargs):
        self.send(loc.FORM_FIRSTNAME, kwargs.get('firstname'))
        self.send(loc.FORM_LASTNAME, kwargs.get('lastname'))
        self.send(loc.FORM_EMAIL, kwargs.get('email'))
        self.send(loc.FORM_PASSWORD, kwargs.get('password'))
        self.send(loc.FORM_PASSWORD_CONFIRM, kwargs.get('password'))
        self.find(loc.FORM_SUBMIT).submit()
