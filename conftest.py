
import pytest
from selenium import webdriver as selenium_webdriver
from webdriver_manager.chrome import ChromeDriverManager
from appium import webdriver as appium_webdriver


# Фикстура для Selenium
@pytest.fixture(scope="function")
def selenium_driver():
    print('Start Selenium Fixture')
    sel_driver = selenium_webdriver.Chrome(ChromeDriverManager().install())
    sel_driver.maximize_window()
    yield sel_driver
    sel_driver.quit()


# Фикстура для Appium
@pytest.fixture(scope="function")
def appium_driver():
    print('Start Appium Fixture')
    capabilities = dict(
        platformName='android',
        automationName='uiautomator2',
        deviceName=''
    )

    app_driver = appium_webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
    yield app_driver
    app_driver.quit()



"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    '''Опции командной строки.
    В командную строку передается параметр вида '--language="es"'
    По умолчанию передается параметр, включающий английский интерфейс в браузере
    '''
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ---")


@pytest.fixture(scope="function")
def browser(request):
    print("___USE MAIN FIXTURE__")
    print("\nstart browser for test..")
    options = Options()
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
"""