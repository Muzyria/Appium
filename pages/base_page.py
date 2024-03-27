import time
import os
import subprocess
import time
from datetime import datetime, timedelta
import re

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import pyautogui


# class BasePage:
#     def __init__(self, browser, url, timeout=10):
#         self.browser = browser
#         self.url = url
#         self.browser.implicitly_wait(timeout)
#
#     def open(self):
#         self.browser.get(self.url)
#         self.browser.maximize_window()

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def element_is_visible(self, locator, timeout=30):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=30):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=30):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=30):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=30):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=30):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def move_coursor_to_elrment(self, element):
        div_rect = element.rect
        # Получаем координаты центра элемента
        center_x = div_rect['x'] + div_rect['width'] // 2
        center_y = div_rect['y'] + div_rect['height'] // 2
        # Перемещаем курсор в центр элемента
        pyautogui.moveTo(center_x, center_y, duration=0.5)

    def scroll_element_by_mouse(self, element):
        div_rect = element.rect
        # Получаем координаты центра элемента
        center_x = div_rect['x'] + div_rect['width'] // 2
        center_y = div_rect['y'] + div_rect['height'] // 2
        # Перемещаем курсор в центр элемента
        pyautogui.moveTo(center_x, center_y, duration=0.5)
        # Выполняем прокрутку колесика мыши
        pyautogui.scroll(-500)
        time.sleep(1)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()


class AppiumBasePage:
    def __init__(self, appium_driver):
        self.appium_driver = appium_driver

    def element_is_visible(self, locator, timeout=30):
        return wait(self.appium_driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=30):
        return wait(self.appium_driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=30):
        return wait(self.appium_driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=30):
        return wait(self.appium_driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=30):
        return wait(self.appium_driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=30):
        return wait(self.appium_driver, timeout).until(EC.element_to_be_clickable(locator))

    def touch_action(self, coordinate):
        action = TouchAction(self.appium_driver)
        action.tap(x=coordinate[0], y=coordinate[1]).perform()

    def swipe_screen_with_coordinate(self, start_coordinate=None, end_coordinate=None, duration=1000):  # Продолжительность свайпа в миллисекундах
        print(self.appium_driver.get_window_size()['width'])
        print(self.appium_driver.get_window_size()['height'])
        self.appium_driver.swipe(start_coordinate[0], start_coordinate[1], end_coordinate[0], end_coordinate[1], duration)

    def swipe_screen_down(self, duration=200):  # Продолжительность свайпа в миллисекундах
        start_x = self.appium_driver.get_window_size()['width'] // 2
        start_y = self.appium_driver.get_window_size()['height'] * 0.8
        end_y = self.appium_driver.get_window_size()['height'] * 0.2
        self.appium_driver.swipe(start_x, start_y, start_x, end_y, duration)  # Прокрутка вниз
        time.sleep(1)

    def swipe_screen_up(self, duration=200):  # Продолжительность свайпа в миллисекундах
        start_x = self.appium_driver.get_window_size()['width'] // 2
        start_y = self.appium_driver.get_window_size()['height'] * 0.8
        end_y = self.appium_driver.get_window_size()['height'] * 0.2
        self.appium_driver.swipe(start_x, end_y, start_x, start_y, duration)  # Прокрутка вверх
        time.sleep(1)

    def press_key(self, key):
        """
        MENU = 187
        EMERGENCY = 4
        MAIN_BUTTON = 3 #
        VOLUME = 24, 25
        BLUETOOTH = 131
        """
        self.appium_driver.press_keycode(key)

    def long_press_key(self, key):
        """
        MAIN_MENU = 26
        """
        self.appium_driver.long_press_keycode(key)

    def take_screenshot(self, file_name, extra_name=''):     # Пример использования: self.take_screenshot('screenshot.png')
        path_directory = 'screenshots/'
        try:
            self.appium_driver.save_screenshot(f"{path_directory}{file_name}{extra_name}.jpg")
            print(f"Скриншот сохранен: {file_name}")
        except Exception as e:
            print(f"Ошибка при создании скриншота: {e}")

    def take_element_screenshot(self, locator, file_name, extra_name=''): # Пример использования:  # self.take_element_screenshot((MobileBy.ID, 'element_id'), 'element_screenshot.png')
        path_directory = 'screenshots/'
        try:
            element = self.element_is_visible(locator)
            element.screenshot(f"{path_directory}{file_name}{extra_name}.jpg")
            print(f"Скриншот элемента сохранен: {file_name}")
        # except TimeoutException:
        #     print(f"Элемент {locator} не найден для создания скриншота.")
        except Exception as e:
            print(f"Ошибка при создании скриншота элемента: {e}")

    def check_element_is_visible(self, locator):
        try:
            element = self.element_is_visible(locator)
            # Проверка видимости элемента
            if element.is_displayed():
                print("Элемент видим на экране")
            # Проверка активности элемента
            if element.is_enabled():
                print("Элемент активен")
            return True
        except(Exception):
            print('Элемент не найден')
            return False


class AdbCommands:
    def __init__(self, ip_device=None):
        self.ip_device = ip_device

    @staticmethod
    def device_read_ip_address():
        """Получение IP адрес девайса при подключении по USB"""
        os.system(fr'adb shell ip addr show wlan0')  # читаем IP девайса
        result = subprocess.run(["adb", "shell", "ip", "addr", "show", "wlan0"], capture_output=True, text=True)
        output_lines = result.stdout.splitlines()

        # Регулярное выражение для извлечения IP-адреса
        pattern = r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        ip_address = re.search(pattern, [item for item in output_lines if 'inet ' in item][0]).group(0).split()[1]
        print(ip_address)
        return ip_address

    def adb_get_state(self):
        output = os.system('adb get-state')
        # print(f'{output}')
        return output

    def device_disconnect(self):
        os.system(f'adb disconnect {self.ip_device}')

    def device_connect(self):
        os.system(f'adb connect {self.ip_device}')

    def device_reboot(self):
        os.system(f'adb -s {self.ip_device} reboot')

    def check_devices_active(self):
        """Проверяем, есть ли подключенные устройства в выводе в консоль"""
        output = subprocess.check_output(['adb', 'devices'])
        if self.ip_device in str(output) and "offline" not in str(output):
            print('Устройство Android подключено и активно.')

        else:
            print(f'Устройство Android {self.ip_device} будет подключено By TCP/IP')
            self.device_disconnect()
            time.sleep(2)
            self.device_connect()

    def device_send_key(self, key=26):
        os.system(f'adb -s {self.ip_device} shell input keyevent {key}')

    def touch_screen(self, x=700, y=500):
        os.system(f'adb -s {self.ip_device} shell input tap {x} {y}')

    def device_send_coordinate(self, location):
        os.system(rf'adb -s {self.ip_device}:5555 shell am broadcast -a ua.org.jeff.mockgps.ACTION_LOCATION --es location \"{location}\"')  # "50.012356,36.243361"

    def device_in_cart_barn(self):
        os.system(f'adb -s {self.ip_device} shell am broadcast -a com.l1inc.yamatrack3d.action.powermanagement.cart_barn_sleep')

    def device_in_off_hole(self):
        os.system(f'adb -s {self.ip_device} shell am broadcast -a com.l1inc.yamatrack3d.action.powermanagement.not_on_hole_sleep')

    def device_close_yamatack(self):
        os.system(f'adb -s {self.ip_device} shell am force-stop com.l1inc.yamatrack3d')

    def device_close_all(self):
        os.system(f'adb -s {self.ip_device} shell input keyevent KEYCODE_HOME')

    def device_kill_app(self):
        os.system(f'adb -s {self.ip_device} shell input keyevent KEYCODE_APP_SWITCH')
        os.system(f'adb -s {self.ip_device} shell input keyevent DEL')

    def device_get_system_volume_speaker(self):
        """Get value system volume speaker"""
        os.system(f'adb -s {self.ip_device} shell settings get system volume_alarm_speaker')

    """SETTINGS PAGES"""
    def device_open_settings_main_page(self):
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.SETTINGS')

    def device_open_wifi_settings(self):
        """Open pages Settings WI-FI"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.WIFI_SETTINGS')

    def device_open_wireless_settings(self):
        """Open pages Settings WireLess"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.WIRELESS_SETTINGS')

    def device_open_sounds_settings(self):
        """Open pages Settings Sounds"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.SOUND_SETTINGS')

    def device_open_location_settings(self):
        """Open pages Settings Location"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.LOCATION_SOURCE_SETTINGS')

    def open_date_settings(self):
        """Open pages Settings Date"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.DATE_SETTINGS')

    def open_device_info_settings(self):
        """Open pages Settings Device Info"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.DEVICE_INFO_SETTINGS')

    def open_device_developer_options_settings(self):
        """Open pages Settings Developer Options"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.APPLICATION_DEVELOPMENT_SETTINGS')
