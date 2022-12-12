from pages.eco_friendly import EcoFriendlyPage


def test_max_12_items_are_displayed_on_the_page(driver):
    eco = EcoFriendlyPage(driver)
    eco.open()
    assert eco.products_count() == 12


def test_max_24_items_are_displayed_on_the_page(driver):
    eco = EcoFriendlyPage(driver)
    eco.open()
    eco.click_24_items()
    assert eco.products_count() == 18


def test_no_items_to_compare(driver):
    eco = EcoFriendlyPage(driver)
    eco.open()
    assert eco.compare_text() == 'You have no items to compare.'
