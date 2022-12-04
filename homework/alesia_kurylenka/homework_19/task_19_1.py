from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def open_browser():
    options = Options()
    options.add_argument('window-size=400,1000')
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(5)
    return chrome_driver


def demoqa(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    first_name = driver.find_element(By.ID, 'firstName')
    first_name.send_keys('Alesia')

    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys('Kurylenka')

    email_field = driver.find_element(By.ID, 'userEmail')
    email_field.send_keys('name@example.com')

    femail_button = driver.find_element(By.XPATH, '//label[@for="gender-radio-2"]')
    femail_button.click()

    user_number = driver.find_element(By.ID, 'userNumber')
    user_number.send_keys('1111111111')
    driver.execute_script("window.scrollTo(0, 600);")
    user_birth = driver.find_element(By.ID, 'dateOfBirthInput')
    user_birth.click()

    month_button = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select')
    month_button.click()

    choose_month = driver.find_element(By.XPATH, '//option[@value="1"]')
    choose_month.click()

    year_button = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select')
    year_button.click()
    choose_year = driver.find_element(By.XPATH, '//option[@value="1994"]')
    choose_year.click()

    day_button = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__day--014')
    day_button.click()

    subject_field = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
    subject_field.click()
    subject_field.send_keys("automation practice")
    subject_field.send_keys(Keys.END)

    hobby_button = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]')
    hobby_button.click()

    add_file = driver.find_element(By.XPATH, '//input[@id="uploadPicture"]')
    add_file.send_keys("C:/aqa_python_part2/QAP-10onl/homework/alesia_kurylenka/homework_19/picture_task_19.png")

    address = driver.find_element(By.ID, 'currentAddress')
    address.send_keys("Testing street, 22")

    select_state_field = driver.find_element(By.ID, 'state')
    select_state_field.click()
    select_state = driver.find_element(By.ID, 'react-select-3-input')
    select_state.send_keys('Uttar Pradesh')
    select_state.send_keys(Keys.ENTER)

    select_city_field = driver.find_element(By.ID, 'city')
    select_city_field.click()
    select_city = driver.find_element(By.ID, 'react-select-4-input')
    select_city.send_keys('Merrut')
    select_state.send_keys(Keys.ENTER)

    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.submit()

    page_text = driver.find_element(By.CSS_SELECTOR, '.modal-content')
    print(page_text.text)


common_driver = open_browser()
demoqa(common_driver)
common_driver.quit()
