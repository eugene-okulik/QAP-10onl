from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.page_url = ''

    def open(self):
        self.driver.get(self.page_url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        return self.find(locator).click()

    def send(self, locator, value):
        return self.find(locator).send_keys(value)
