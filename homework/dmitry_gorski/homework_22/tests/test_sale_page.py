import pytest
from pages.sale_page import SalePage


@pytest.mark.smoke
def test_page_is_open(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    assert sale_page.is_open == 'Sale'


@pytest.mark.simple
def test_compare_count_of_items(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    sale_page.click_to_elem()
    assert sale_page.count_of_items() == 12


@pytest.mark.hard
def test_valid_background(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    assert sale_page.get_color == '#71b54e'
