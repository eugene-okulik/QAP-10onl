from selenium.webdriver.common.by import By


title_text = (By.CLASS_NAME, 'base')
my_cart = (By.XPATH, '//span[normalize-space(text())="My Cart"]')
products = (By.CSS_SELECTOR, 'img[class="product-image-photo"]')
