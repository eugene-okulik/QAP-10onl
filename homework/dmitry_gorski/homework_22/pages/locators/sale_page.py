from selenium.webdriver.common.by import By


PAGE_TITLE = (By.TAG_NAME, 'h1')
JACKET_LINK = (By.LINK_TEXT, 'Jackets')
ITEMS_LIST = (By.XPATH, '//li[@class="item product product-item"]')
FREE_SALES = (By.XPATH, '//a[@class="block-promo sale-free-shipping"]')
