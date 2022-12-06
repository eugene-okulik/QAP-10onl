from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


def driver():
    options = Options()
    options.add_argument('window-size=400,1000')
    driver_chrome = webdriver.Chrome(options=options)
    driver_chrome.implicitly_wait(10)
    return driver_chrome


def filling_the_form(driver_chrome):
    driver_chrome.get('https://demoqa.com/automation-practice-form')

    first_name = driver_chrome.find_element(By.ID, 'firstName')
    first_name.send_keys('Kazimir')

    last_name = driver_chrome.find_element(By.ID, 'lastName')
    last_name.send_keys('Malevich')

    email = driver_chrome.find_element(By.ID, 'userEmail')
    email.send_keys('malevichkazimir@gmail.com')

    gender = driver_chrome.find_elements(By.CLASS_NAME, 'custom-control-label')
    gender[0].click()

    mobile_number = driver_chrome.find_element(By.ID, 'userNumber')
    mobile_number.send_keys('1234567893')

    driver_chrome.execute_script("window.scrollTo(0, 600);")

    date_of_birth = driver_chrome.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth.click()

    year = Select(driver_chrome.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
    year.select_by_value('1979')

    month = Select(driver_chrome.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
    month.select_by_value('1')

    day = driver_chrome.find_element(By.CSS_SELECTOR, '.react-datepicker__day--023')
    day.click()

    driver_chrome.execute_script("window.scrollTo(0,800);")

    hobbies = driver_chrome.find_elements(By.CSS_SELECTOR,
                                          '.custom-control.custom-checkbox.custom-control-inline')
    hobbies[1].click()

    current_address = driver_chrome.find_element(By.ID, 'currentAddress')
    current_address.send_keys('55 ° 43′17 ″ s. Sh. 37 ° 20′17 ″ c. D.')
    current_address.send_keys(Keys.END)

    state_window = driver_chrome.find_element(By.ID, 'state')
    state = state_window.find_element(By.XPATH, '//input[@id="react-select-3-input"]')
    state.send_keys('Haryana')
    state.send_keys(Keys.ENTER)

    city_window = driver_chrome.find_element(By.ID, 'city')
    city = city_window.find_element(By.XPATH, '//input[@id="react-select-4-input"]')
    city.send_keys('Karnal')
    city.send_keys(Keys.ENTER)

    driver_chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    submit = driver_chrome.find_element(By.ID, 'submit')
    submit.submit()

    print(driver_chrome.find_element(By.CLASS_NAME, 'modal-content').text)


driver_chrome = driver()
filling_the_form(driver_chrome)
driver_chrome.quit()
