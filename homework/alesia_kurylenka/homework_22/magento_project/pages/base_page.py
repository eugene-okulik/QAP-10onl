from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def zoom_out_by_two(self):
        self.driver.execute_script("document.body.style.zoom = '0.5'")

    def click(self, locator):
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        element.click()
