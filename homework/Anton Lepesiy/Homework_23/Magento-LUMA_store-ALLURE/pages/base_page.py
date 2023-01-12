from selenium.webdriver.chrome.webdriver import WebDriver


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
        return self.find(*locator).click()

    def find_and_submit(self, locator):
        return self.find(*locator).submit()

    def send_key(self,  keys):
        return self.send_key(keys)
