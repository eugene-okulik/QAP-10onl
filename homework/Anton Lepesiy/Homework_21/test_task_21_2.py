from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


URL = 'https://demoqa.com/menu#'


def test_sublist_check(driver):
    driver.get(URL)
    main_item_2 = driver.find_element(By.XPATH, '//a[text()="Main Item 2"]')
    sub_sub_list = driver.find_element(By.XPATH, '//a[text()="SUB SUB LIST »"]')
    sub_sub_item_2 = driver.find_element(By.XPATH, '//a[text()="Sub Sub Item 2"]')
    WebDriverWait(driver, 10).until(EC.visibility_of(main_item_2))
    action = ActionChains(driver)
    action.move_to_element(main_item_2)
    WebDriverWait(driver, 1)
    action.move_to_element(sub_sub_list)
    WebDriverWait(driver, 1)
    action.move_to_element(sub_sub_item_2)
    WebDriverWait(driver, 1)
    action.perform()
