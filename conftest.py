
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from appium import webdriver as appium_webdriver


device_name = "192.168.0.103"


def pytest_addoption(parser):
    """Опции командной строки.
    В командную строку передается параметр вида '--language="es"'
    По умолчанию передается параметр, включающий английский интерфейс в браузере
    """
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ---")


@pytest.fixture(scope="function")
def driver(request):
    """selenium fixture"""
    print("__USE_SELENIUM_FIXTURE__")
    print("\nstart driver for test..")
    options = Options()
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    print("\nquit driver..")
    driver.quit()


# Фикстура для Appium
@pytest.fixture(scope="function")
def appium_driver():
    """appium fixture"""
    print('__USE_APPIUM_FIXTURE__')
    print("\nstart appium_driver for test..")
    capabilities = dict(
        platformName='android',
        automationName='uiautomator2',
        deviceName=device_name
    )
    appium_driver = appium_webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
    yield appium_driver
    print("\nquit appium_driver..")
    appium_driver.quit()

