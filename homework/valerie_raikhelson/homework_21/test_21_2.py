from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://demoqa.com/menu#'


def test_hover(driver):
    driver.get(URL)
    main_item_2 = driver.find_element(By.CSS_SELECTOR, '#nav>:nth-child(2)>a')
    list_elem = driver.find_elements(By.CSS_SELECTOR, '#nav>:nth-child(2)>ul>li')
    sub_sub_list = list_elem[2]
    sub_sub_item_2 = sub_sub_list.find_element(By.CSS_SELECTOR, 'li:nth-child(2)>a')

    action = ActionChains(driver)
    action.move_to_element(main_item_2).move_to_element(sub_sub_list).move_to_element(sub_sub_item_2).perform()
