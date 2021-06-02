from pages.locators import BasePageLocators
from pages.main_page import MainPage


def test_footer_is_visible(browser):
    page = MainPage(browser, MainPage.URL)
    page.open_page()

    assert browser.find_element(*BasePageLocators.FOOTER)
