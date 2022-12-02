import unittest
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestUnittest(unittest.TestCase):
    driver = None

    def setUp(self) -> None:
        print('Before test')
        options = Options()
        options.add_argument('start-maximized')
        # options.add_argument('window-size=1000,600')
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        print('After test')
        self.driver.quit()

    def test_tabs(self):
        print('I am a test')
        self.driver.get('https://the-internet.herokuapp.com/windows')
        link = self.driver.find_element(By.LINK_TEXT, 'Click Here')
        link.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        print(self.driver.find_element(By.TAG_NAME, 'h3').text)
        self.driver.switch_to.window(self.driver.window_handles[0])
        print(self.driver.find_element(By.TAG_NAME, 'h3').text)

    def test_sum(self):
        print('test sum')
        self.assertEqual(2 + 2, 5, msg='sum is incorrect')

    @unittest.skip('Bug #234')
    def test_xum(self):
        print('test xum')
        self.assertEqual(2 + 2, 6)

    @unittest.skipIf(datetime.now().year == 2021, 'Not supported in 2022')
    def test_wum(self):
        print('test wum')
        self.assertTrue(2 + 2 < 5)
