from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        raise NotImplementedError

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_s(self, locator):
        return self.driver.find_element(*locator)
