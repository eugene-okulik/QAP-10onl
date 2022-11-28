from common.utils import WebPage

page = WebPage()
page.DRIVER.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
page.find_by_id('isAgeSelected').click()
print(page.find_by_id('txtAge').text)
page.DRIVER.quit()
