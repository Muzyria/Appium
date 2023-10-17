import pytest
from selenium import webdriver as selenium_webdriver
from webdriver_manager.chrome import ChromeDriverManager
from appium import webdriver as appium_webdriver


# Фикстура для Selenium
@pytest.fixture(scope="function")
def selenium_driver():
    selenium_driver = selenium_webdriver.Chrome(ChromeDriverManager().install())
    selenium_driver.maximize_window()
    yield selenium_driver
    selenium_driver.quit()


# Фикстура для Appium
@pytest.fixture(scope="function")
def appium_driver():
    capabilities = dict(
        platformName='android',
        automationName='uiautomator2',
        deviceName='192.168.3.221'
    )

    appium_driver = appium_webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    yield appium_driver
    appium_driver.quit()
