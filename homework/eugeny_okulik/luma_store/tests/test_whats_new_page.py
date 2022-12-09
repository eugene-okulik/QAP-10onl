from pages.whats_new_page import WhatsNewPage


def test_products_count(driver):
    whats_new = WhatsNewPage(driver)
    whats_new.open()
    assert whats_new.products_count() == 4


def test_no_items_to_compare(driver):
    whats_new = WhatsNewPage(driver)
    whats_new.open()
    assert whats_new.compare_text() == 'You have no items to compare.'
