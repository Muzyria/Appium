import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import pyautogui

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

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
    def __init__(self, driver):
        self.driver = driver

    def element_is_visible(self, locator, timeout=30):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def touch_action(self, coordinate):
        action = TouchAction(self.driver)
        action.tap(x=coordinate[0], y=coordinate[1]).perform()

    def swipe_screen_with_coordinate(self, start_coordinate=None, end_coordinate=None, duration=1000):  # Продолжительность свайпа в миллисекундах
        print(self.driver.get_window_size()['width'])
        print(self.driver.get_window_size()['height'])
        self.driver.swipe(start_coordinate[0], start_coordinate[1], end_coordinate[0], end_coordinate[1], duration)

    def swipe_screen_down(self, duration=200):  # Продолжительность свайпа в миллисекундах
        start_x = self.driver.get_window_size()['width'] // 2
        start_y = self.driver.get_window_size()['height'] * 0.8
        end_y = self.driver.get_window_size()['height'] * 0.2
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)  # Прокрутка вниз
        time.sleep(1)

    def swipe_screen_up(self, duration=200):  # Продолжительность свайпа в миллисекундах
        start_x = self.driver.get_window_size()['width'] // 2
        start_y = self.driver.get_window_size()['height'] * 0.8
        end_y = self.driver.get_window_size()['height'] * 0.2
        self.driver.swipe(start_x, end_y, start_x, start_y, duration)  # Прокрутка вверх
        time.sleep(1)

    def press_key(self, key):
        """
        MENU = 187
        EMERGENCY = 4
        MAIN_BUTTON = 3 #
        VOLUME = 24, 25
        BLUETOOTH = 131
        """
        self.driver.press_keycode(key)

    def long_press_key(self, key):
        """
        MAIN_MENU = 26
        """
        self.driver.long_press_keycode(key)

    def take_screenshot(self, file_name, extra_name=''):     # Пример использования: self.take_screenshot('screenshot.png')
        path_directory = 'screenshots/'
        try:
            self.driver.save_screenshot(f"{path_directory}{file_name}{extra_name}.jpg")
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
