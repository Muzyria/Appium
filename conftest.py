
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from appium import webdriver as appium_webdriver


def pytest_addoption(parser):
    """Опции командной строки.
    В командную строку передается параметр вида '--language="es"'
    По умолчанию передается параметр, включающий английский интерфейс в браузере
    """
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ---")


@pytest.fixture(scope="function")
def browser(request):
    """selenium fixture"""
    print("__USE_SELENIUM_FIXTURE__")
    print("\nstart browser for test..")
    options = Options()
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


# Фикстура для Appium
@pytest.fixture(scope="function")
def appium_driver():
    """appium fixture"""
    print('__USE_APPIUM_FIXTURE__')
    capabilities = dict(
        platformName='android',
        automationName='uiautomator2',
        deviceName='192.168.2.33'
    )

    app_driver = appium_webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
    yield app_driver
    app_driver.quit()
