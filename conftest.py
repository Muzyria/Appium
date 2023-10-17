# import pytest
# from selenium import webdriver as selenium_webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from appium import webdriver as appium_webdriver
# from appium.webdriver.common.appiumby import AppiumBy
#
#
# # # Фикстура для Selenium
# # @pytest.fixture(scope="function")
# # def selenium_driver():
# #     sel_driver = selenium_webdriver.Chrome(ChromeDriverManager().install())
# #     sel_driver.maximize_window()
# #     yield sel_driver
# #     sel_driver.quit()
#
#
# # Фикстура для Appium
# @pytest.fixture(scope="function")
# def appium_driver():
#     capabilities = dict(
#         platformName='android',
#         automationName='uiautomator2',
#         deviceName='192.168.3.221'
#     )
#
#     driver = appium_webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
#     yield driver
#     driver.quit()
#
# def test_appium_example(appium_driver):
#     el = appium_driver.find_element(by=AppiumBy.ID, value='com.l1inc.yamatrack3d:id/buttonMenu')
#     el.click()
# import pytest
# from appium import webdriver
# from appium.webdriver.common.mobileby import AppiumBy
#
# capabilities = {
#     'platformName': 'android',
#     'automationName': 'uiautomator2',
#     'deviceName': '192.168.3.221'
# }
#
# appium_server_url = 'http://127.0.0.1:4723/wd/hub'
#
# @pytest.fixture(scope="function")
# def appium_driver():
#     driver = webdriver.Remote(appium_server_url, capabilities)
#     yield driver
#     driver.quit()
#
# def test_find_battery(appium_driver):
#     el = appium_driver.find_element(by=AppiumBy.ID, value='com.l1inc.yamatrack3d:id/buttonMenu')
#     el.click()
import os
import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import By


# os.system(f'adb connect 192.168.3.221')
#
# capabilities = dict(
#     platformName='android',
#     automationName='uiautomator2',
#     deviceName='192.168.3.221'
# )
#
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
# driver.implicitly_wait(10)