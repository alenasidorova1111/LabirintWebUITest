import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en, ru, etc...")


@pytest.fixture(scope="module")
def browser(request):
    """
    Sets browser with the following settings.

    :param request: built-in pytest fixture
    :return: browser with settings
    Browser closes in the teardown part of this fixture.

    You may also:
        - add browser.implicitly_wait(seconds_amount) if you need to wait before every
        action of browser.
        - change options.add_argument("--headless") for options.headless = True

    ATTENTION!! You need to delete params executable_path in initialization of browser if
    you need to run tests from command line!

    """
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_argument("--headless")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(executable_path='C:/Users/AlenaStudent/chromedriver.exe', options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp, executable_path=r"C:\Users\AlenaStudent\geckodriver.exe")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    print("\nquit browser..")
    browser.quit()
