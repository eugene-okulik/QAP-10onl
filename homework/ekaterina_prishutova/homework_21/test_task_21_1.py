from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LINK_DEMOBLASE = 'https://www.demoblaze.com/index.html'
LINK_DEMOQA = 'https://demoqa.com/menu#'
LINK_TESTPAGES = 'https://testpages.herokuapp.com/styled/alerts/alert-test.html'


def move_between_windows(driver, url):
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if driver.current_url == url:
            break
    return driver


def test_add_to_cart(driver):
    driver.get(LINK_DEMOBLASE)
    product = driver.find_element(By.XPATH, '//div[@id="tbodyid"]/div[1]/div/div/h4/a')
    product_href = product.get_attribute("href")
    product_name = product.text
    product.send_keys(Keys.COMMAND + Keys.SHIFT + Keys.ENTER)

    driver = move_between_windows(driver, product_href)

    add_to_cart_button = driver.find_element(By.XPATH, '//a[@class="btn btn-success btn-lg"]')
    add_to_cart_button.click()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    driver.close()

    driver = move_between_windows(driver, LINK_DEMOBLASE)
    cart = driver.find_element(By.XPATH, '//a[@id="cartur"]')
    cart.click()
    assert driver.find_element(By.XPATH, '//tr[@class="success"]/td[2]').text == product_name


def test_demoqa(driver):
    driver.get(LINK_DEMOQA)
    main_item_2 = driver.find_element(By.XPATH, '//ul[@id="nav"]/li[2]/a')
    sub_sub_list = driver.find_element(By.XPATH, '//ul[@id="nav"]/li[2]/ul/li[3]/a')
    sub_sub_item_2 = driver.find_element(By.XPATH, '//ul[@id="nav"]/li[2]/ul/li[3]/ul/li[2]/a')
    ActionChains(driver).move_to_element(main_item_2).move_to_element(sub_sub_list).click(sub_sub_item_2).perform()


def test_alert(driver):
    test_text = 'ololo'
    driver.get(LINK_TESTPAGES)
    prompt_button = driver.find_element(By.XPATH, '//input[@id="promptexample"]')
    prompt_button.click()
    driver.switch_to.alert.send_keys(test_text)
    driver.switch_to.alert.accept()
    assert driver.find_element(By.XPATH, '//p[@id="promptreturn"]').text == test_text
