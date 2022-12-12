from pages.home_page import HomePage
from pages.whats_new_page import WhatsNewPage


def test_whats_new_link(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.click_whats_new_link()
    # home_page.whats_new_link.click()
    whats_new_page = WhatsNewPage(driver)
    assert whats_new_page.is_page_opened()
