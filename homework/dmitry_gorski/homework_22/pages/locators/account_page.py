from selenium.webdriver.common.by import By


PAGE_TITLE = (By.TAG_NAME, 'h1')
SUBSCRIBE_CHECKBOX = (By.ID, 'is_subscribed')

FORM_FIRSTNAME = (By.ID, 'firstname')
FORM_LASTNAME = (By.ID, 'lastname')
FORM_EMAIL = (By.ID, 'email_address')
FORM_PASSWORD = (By.ID, 'password')
FORM_PASSWORD_CONFIRM = (By.ID, 'password-confirmation')
FORM_SUBMIT = (By.XPATH, '//button[@type="submit"]')
