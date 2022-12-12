from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_hovers(driver):
    driver.get('https://demoqa.com/menu#')
    main_item_2 = driver.find_element(By.XPATH, '//ul[@id="nav"]//li[2]')
    sub_sub_list = driver.find_element(By.XPATH, '//a[text()="SUB SUB LIST »"]')
    sub_sub_item_2 = driver.find_element(By.XPATH, '//a[text()="Sub Sub Item 2"]')
    WebDriverWait(driver, 10).until(EC.visibility_of(main_item_2))
    actions = ActionChains(driver)
    actions.move_to_element(main_item_2)
    actions.move_to_element(sub_sub_list)
    actions.move_to_element(sub_sub_item_2)
    actions.perform()
