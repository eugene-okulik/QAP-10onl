from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

link = 'https://demoqa.com/menu#'


def test_two(driver):
    driver.get(link)
    action = ActionChains(driver)
    elem, sub_elem_1, sub_elem_2 = driver.find_element(By.XPATH, '//a[text() = "Main Item 2"]'), driver.find_element(
        By.XPATH, '//a[text() = "SUB SUB LIST »"]'), driver.find_element(By.XPATH, '//a[text() = "Sub Sub Item 2"]')
    action.move_to_element(elem)
    action.move_to_element(sub_elem_1)
    action.move_to_element(sub_elem_2)
    action.perform()
