from selenium.webdriver.common.by import By


page_title = (By.TAG_NAME, 'h1')
products_list = (By.CSS_SELECTOR, '.product-item')
empty_items_to_compare = (By.XPATH, '//div[@class="block block-compare"]/div[2]')
