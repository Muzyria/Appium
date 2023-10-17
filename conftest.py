import time

import pytest
from selenium import webdriver as selenium_webdriver
from webdriver_manager.chrome import ChromeDriverManager
from appium import webdriver as appium_webdriver
from appium.webdriver.common.appiumby import AppiumBy


# Фикстура для Selenium
@pytest.fixture(scope="function")
def selenium_driver():
    sel_driver = selenium_webdriver.Chrome(ChromeDriverManager().install())
    sel_driver.maximize_window()
    yield sel_driver
    sel_driver.quit()

# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait as wait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class BasePage:
#     def __init__(self, driver, url):
#         self.driver = driver
#         self.url = url
#
#     def open(self):
#         self.driver.get(self.url)
#
#
# def test(selenium_driver):
#     page = BasePage(selenium_driver, 'https://google.com')
#     page.open()
#     time.sleep(3)




# # Фикстура для Appium
# @pytest.fixture(scope="function")
# def appium_driver():
#     capabilities = dict(
#         platformName='android',
#         automationName='uiautomator2',
#         deviceName=''
#     )
#
#     app_driver = appium_webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
#     yield app_driver
#     app_driver.quit()


# def test_appium_example(appium_driver):
#     el = appium_driver.find_element(by=AppiumBy.ID, value='com.l1inc.yamatrack3d:id/buttonMenu')
#     el.click()
