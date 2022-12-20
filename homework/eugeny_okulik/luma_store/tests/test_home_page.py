from pages.home_page import HomePage
from pages.whats_new_page import WhatsNewPage
import allure


@allure.feature('Home page')
@allure.story('Site header links')
@allure.title('Проверка ссылки whats new')
def test_whats_new_link(driver):
    with allure.step('Open Home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Click what\'s new link'):
        home_page.click_whats_new_link()
    # home_page.whats_new_link.click()
    with allure.step('Check that Wahat\'s new page is opened'):
        whats_new_page = WhatsNewPage(driver)
        assert whats_new_page.is_page_opened
