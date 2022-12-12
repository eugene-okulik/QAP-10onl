from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.page_url = ''

    def open(self):
        if self.page_url:
            self.driver.get(self.page_url)
        else:
            raise NotImplementedError

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        element.click()

    def set_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.send_keys(text)

    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    def is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def is_selected(self, locator):
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_selected(element))
        return element.is_selected()

    def switch_tab(self, tab):
        self.driver.switch_to.window(self.driver.window_handles[tab])

    def accept_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        Alert(self.driver).accept()

    def scroll_to_the_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_current_url(self):
        return self.driver.current_url

    def select_by_value(self, locator, value):
        select = Select(self.driver.find_element(*locator))
        select.select_by_value(value)
