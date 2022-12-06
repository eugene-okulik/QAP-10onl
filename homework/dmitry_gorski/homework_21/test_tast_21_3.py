from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

link = 'https://testpages.herokuapp.com/styled/alerts/alert-test.html'
my_input = 'Realy? You promt me?'


def test_three(driver):
    driver.get(link)
    driver.find_element(By.ID, 'promptexample').click()
    Alert(driver).send_keys(str(my_input))
    Alert(driver).accept()
    assert my_input in driver.find_element(By.ID, 'promptreturn').text
