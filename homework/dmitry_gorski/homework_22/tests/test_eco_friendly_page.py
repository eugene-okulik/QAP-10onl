import pytest
from pages.eco_friendly_page import EcoFriendlyPage


@pytest.mark.smoke
def test_page_is_open(driver):
    eco_friendly_page = EcoFriendlyPage(driver)
    eco_friendly_page.open()
    assert eco_friendly_page.is_open == 'Eco Friendly'


@pytest.mark.simple
def test_compare_count_of_items(driver):
    eco_friendly_page = EcoFriendlyPage(driver)
    eco_friendly_page.open()
    assert eco_friendly_page.count_of_items() == 12


@pytest.mark.hard
def test_item_price_in_range(driver):
    eco_friendly_page = EcoFriendlyPage(driver)
    eco_friendly_page.open()
    assert eco_friendly_page.get_price_of_item in ['$45.00', '$30.00', '$40.00']
