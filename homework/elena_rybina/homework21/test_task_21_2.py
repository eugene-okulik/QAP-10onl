from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_two(driver):
    driver.get('https://demoqa.com/menu#')
    main_item_2 = driver.find_element(By.XPATH, '//ul[@id="nav"]/li[2]')
    main_item_2.click()
    sub_sub_list = driver.find_element(By.XPATH, '//ul[@id="nav"]/li[2]/ul/li[3]')
    sub_sub_list.click()
    sub_sub_item = driver.find_element(By.XPATH, '//ul[@id="nav"]/li[2]/ul/li[3]/ul/li[2]')
    sub_sub_item.click()
