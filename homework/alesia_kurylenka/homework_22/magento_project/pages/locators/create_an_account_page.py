from selenium.webdriver.common.by import By


page_title = (By.TAG_NAME, 'h1')
create_account_button = (By.XPATH, '//button[@title="Create an Account"]')
validation_errors = (By.XPATH, '//div[text()="This is a required field."]')
