from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://demoqa.com/menu#'


def test_two(driver):
    driver.get(link)
    action = ActionChains(driver)
    elem, sub_elem_1, sub_elem_2 = driver.find_element(By.XPATH, '//a[text() = "Main Item 2"]'), driver.find_element(
        By.XPATH, '//a[text() = "SUB SUB LIST »"]'), driver.find_element(By.XPATH, '//a[text() = "Sub Sub Item 2"]')
    action.move_to_element(elem).move_to_element(sub_elem_1).move_to_element(sub_elem_2).perform()
    WebDriverWait(driver, 10).until(EC.visibility_of(sub_elem_2))
