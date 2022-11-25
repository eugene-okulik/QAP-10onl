from selenium import webdriver
from selenium.webdriver.common.by import By


class WebPage:

    DRIVER = webdriver.Chrome()

    def __init__(self, webpage: str):
        self.webpage = webpage

    @staticmethod
    def find_by_id(elem_name: str):
        return WebPage.DRIVER.find_element(By.ID, elem_name)

    @staticmethod
    def find_by_class(elem_name: str):
        return WebPage.DRIVER.find_element(By.CLASS_NAME, elem_name)
