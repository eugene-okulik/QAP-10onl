from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        raise NotImplementedError

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def send(self, locator, text):
        return self.find(locator).send_keys(text)

    def click(self, locator):
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(element))
        element.click()

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()
