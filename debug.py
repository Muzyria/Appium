import os
import time
from appium import webdriver
from appium.webdriver.common.mobileby import AppiumBy
from appium.webdriver.common.appiumby import By

# os.system(f'adb disconnect')
# os.system(f'adb connect 192.168.0.103')

capabilities = dict(
    platformName='android',
    automationName='uiautomator2',
    deviceName='192.168.0.103'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
driver.implicitly_wait(10)

# element_name = 'com.l1inc.yamatrack3d:id/textViewName'

driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                    'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                    'android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[7]/'
                                    'android.widget.LinearLayout/android.widget.TextView').click()







