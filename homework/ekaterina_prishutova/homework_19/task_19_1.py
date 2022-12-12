from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def open_browser():
    options = Options()
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    return chrome_driver


def fill_fields(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    field_first_name = driver.find_element(By.ID, "firstName")
    field_first_name.send_keys('firstName')
    field_last_name = driver.find_element(By.ID, "lastName")
    field_last_name.send_keys('lastName')
    field_user_mail = driver.find_element(By.ID, "userEmail")
    field_user_mail.send_keys('userEmail@test.ru')

    checkbox_gender = driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]')
    checkbox_gender.click()

    field_user_number = driver.find_element(By.ID, "userNumber")
    field_user_number.send_keys('79684563214')

    field_date_of_birth = driver.find_element(By.ID, "dateOfBirthInput")
    field_date_of_birth.click()
    select_year = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
    select_year.select_by_value('1990')
    select_month = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
    select_month.select_by_visible_text('June')
    day = driver.find_element(By.XPATH, '//div[@class="react-datepicker__month"]/div[3]/div[1]')
    day.click()

    field_subjects = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
    field_subjects.send_keys('d')
    field_subjects_tab = driver.find_element(By.ID, 'react-select-2-option-0')
    field_subjects_tab.click()

    checkbox_hobbies = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-2"]')
    checkbox_hobbies.click()

    field_current_address = driver.find_element(By.ID, "currentAddress")
    field_current_address.send_keys('currentAddress')

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    select_state = driver.find_element(By.ID, 'state')
    select_state.click()
    sel_state = driver.find_element(By.ID, 'react-select-3-option-0')
    sel_state.click()

    select_city = driver.find_element(By.ID, 'city')
    select_city.click()
    city = driver.find_element(By.ID, 'react-select-4-option-1')
    city.click()

    select_city.submit()

    result_table = driver.find_elements(By.XPATH, '//tbody/tr')
    for i in range(len(result_table)):
        label = driver.find_element(By.XPATH, f'//tbody/tr[{i+1}]/td[1]')
        value = driver.find_element(By.XPATH, f'//tbody/tr[{i+1}]/td[2]')
        print(label.text, ' ', value.text)


common_driver = open_browser()
fill_fields(common_driver)
common_driver.quit()
