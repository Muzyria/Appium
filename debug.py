import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import By


os.system(f'adb disconnect')
os.system(f'adb connect 192.168.2.33')

capabilities = dict(
    platformName='android',
    automationName='uiautomator2',
    deviceName='192.168.2.33'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
driver.implicitly_wait(10)

element_name = '//android.widget.LinearLayout[@content-desc="Startup_Depot,Connected,Wifi signal full."]/android.widget.RelativeLayout'

try:
    # Поиск элемента по имени
    element = driver.find_element(By.XPATH, element_name)

    # Действия с найденным элементом
    element.click()  # Пример действия - кликнуть по элементу

except Exception as e:
    print(f"Ошибка: {e}")
finally:
    # Завершение работы драйвера
    driver.quit()






