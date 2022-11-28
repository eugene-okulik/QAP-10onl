from selenium import webdriver
from selenium.webdriver.common.by import By


class WebPage:

    DRIVER = webdriver.Chrome()

    def find_by_id(self, elem_name: str):
        return self.DRIVER.find_element(By.ID, elem_name)

    def find_by_class(self, elem_name: str):
        return self.DRIVER.find_element(By.CLASS_NAME, elem_name)
