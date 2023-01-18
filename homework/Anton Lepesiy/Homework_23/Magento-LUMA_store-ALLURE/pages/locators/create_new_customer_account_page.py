from selenium.webdriver.common.by import By


PAGE_TITLE = (By.TAG_NAME, 'h1')
CHECK_BOX = (By.CLASS_NAME, 'checkbox')
FIRSTNAME_FIELD_ERROR = (By.ID, 'firstname-error')
SUBMIT_BUTTON = (By.XPATH, '//button[@title="Create an Account"]')
SUBSCRIBE_BUTTON = (By.XPATH, '//button[@title="Subscribe"]')
SUBSCRIBE_FIELD = (By.XPATH, '//input[@placeholder="Enter your email address"]')
EMAIL_ERROR = (By.LINK_TEXT, 'Please enter a valid email address (Ex: johndoe@domain.com).')
