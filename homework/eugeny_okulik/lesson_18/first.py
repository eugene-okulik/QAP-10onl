from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def open_browser():
    options = Options()
    options.add_argument('start-maximized')
    # options.add_argument('window-size=1000,600')
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    # chrome_driver.maximize_window()
    return chrome_driver


def msn(chrome_driver):
    chrome_driver.get('https://www.msn.com/')
    print(chrome_driver.title)
    print(chrome_driver.current_url)


def find_by_id(driver):
    driver.get('https://demoblaze.com/')
    sign_up_link = driver.find_element(By.ID, 'signin2')
    sign_up_link.click()


def by_class_name(driver):
    driver.get('https://demoblaze.com/')
    prev_button = driver.find_element(By.CLASS_NAME, 'carousel-control-prev')
    prev_button.click()


def by_tag_name(driver):
    driver.get('https://demoblaze.com/')
    footer = driver.find_element(By.TAG_NAME, 'footer')
    class_attribute = footer.get_attribute('class')
    print(footer.text)
    print(class_attribute)


common_driver = open_browser()
by_tag_name(common_driver)
sleep(3)
common_driver.quit()
