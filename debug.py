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

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
driver.implicitly_wait(10)


os.system('adb shell am start -a android.settings.DATE_SETTINGS')


date_time_menu = driver.find_element(By.ID, 'com.android.settings:id/list')
print(date_time_menu.__dict__)


set_power_off_time = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[8]')
set_power_off_time.click()

driver.find_element(By.ID, 'android:id/hours').click()
time_hours = driver.find_element(By.XPATH, '//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="4"]').click()
time.sleep(1)
#
driver.find_element(By.ID, 'android:id/minutes').click()
time.sleep(1)
time_minuts = driver.find_element(By.XPATH, '//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="25"]').click()

time.sleep(5)

ok_button = driver.find_element(By.ID, 'android:id/button1').click()