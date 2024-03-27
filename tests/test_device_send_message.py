import time

import pytest

from pages.web_pages.login_page import LoginPage
from pages.web_pages.course_map_page import CourseMapPage

from pages.device_pages.main_screen import MainScreen
from pages.device_pages.menu_screen import MenuScreen
from pages.device_pages.send_massage_screen import SendMessageScreen

from locators.android_locators import SendMessageLocators


@pytest.mark.web
def test_first(driver):
    link = "https://beta.syncwise360.com/login"
    login_page = LoginPage(driver, link)  # инициализируем
    login_page.open()                     # открываем страницу
    login_page.enter_user_to_site()       # входим на сайт
    time.sleep(10)

    course_map_page = CourseMapPage(driver, driver.current_url)
    course_map_page.check_incoming_message()
    time.sleep(10)


@pytest.mark.device
@pytest.mark.parametrize('number_of_message', list(range(1, 9)))
def test_second(appium_driver, number_of_message):
    screen = MainScreen(appium_driver)
    screen.press_button_menu()

    menu_screen = MenuScreen(appium_driver)
    menu_screen.press_button_send_message()

    send_message_screen = SendMessageScreen(appium_driver)
    send_message_screen.send_message(number_of_message)
    send_message_screen.confirm_of_message_sending()
    # send_message_screen.leave_send_message_screen()
    menu_screen.press_button_play_golf()
