from common.utils import WebPage

web, driver = WebPage, WebPage.DRIVER
driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')

web.find_by_id('isAgeSelected').click()
print(web.find_by_id('txtAge').text)
driver.quit()
