from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        raise NotImplementedError

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def send_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.send_keys(text)

    def click(self, locator):
        self.driver.find_element(*locator).click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.driver.find_element(*locator)))

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
