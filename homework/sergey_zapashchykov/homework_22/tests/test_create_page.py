from pages.create_page import CreatePage


def test_get_title_text(driver):
    create_page = CreatePage(driver)
    create_page.open()
    assert create_page.get_element_text() == 'Create New Customer Account'


def test_create_account_button_is_displayed(driver):
    account_button = CreatePage(driver)
    account_button.open()
    account_button.scroll_down()
    assert account_button.element_is_displayed()


def test_required_fields_is_displayed_5(driver):
    required_fields = CreatePage(driver)
    required_fields.open()
    required_fields.scroll_down()
    required_fields.click_element()
    assert required_fields.count_displayed_elements() == 5
