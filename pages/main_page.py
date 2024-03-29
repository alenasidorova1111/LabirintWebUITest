import datetime

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    URL = "https://www.labirint.ru/"

    def get_delivery_date(self, browser):
        page = MainPage(browser, self.URL)
        page.open_page()
        delivery_date_value = browser.execute_script('return arguments[0].textContent;', browser.find_element(*MainPageLocators.DELIVERY_DATE))
        deliv_date = delivery_date_value.strip().split(" ")
        months = {"января": 1, "февраля": 2, "мар": 3, "апр": 4,
                  "мая": 5, "июня": 6, "июл": 7, "авг": 8,
                  "сен": 9, "окт": 10, "ноя": 11, "дек": 12}
        site_date = int(deliv_date[-2])

        site_month = 0
        for k, v in months.items():
            if k.startswith(deliv_date[-1][:3]):
                site_month += v

        return datetime.datetime(datetime.datetime.now().year, int(site_month), site_date)
