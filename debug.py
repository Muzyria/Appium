import os
import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import By


os.system(f'adb connect 192.168.3.221')

capabilities = dict(
    platformName='android',
    automationName='uiautomator2',
    deviceName='192.168.3.221'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
driver.implicitly_wait(10)


os.system('adb shell am start -a android.settings.DATE_SETTINGS')
