import time
import pytest

from pages.web_pages.login_page import LoginPage
from pages.web_pages.course_map_page import CourseMapPage

from pages.device_pages.main_screen import MainScreen
from pages.device_pages.menu_screen import MenuScreen
from pages.device_pages.send_massage_screen import SendMessageScreen


class TestSendMessages:

    @pytest.fixture(scope="session", autouse=True)
    def login_to_site(self, driver):
        link = "https://beta.syncwise360.com/login"
        self.login_page = LoginPage(driver, link)  # инициализируем
        self.login_page.open()  # открываем страницу
        self.login_page.enter_user_to_site()  # входим на сайт
        time.sleep(10)

    @pytest.mark.web
    def test_first(self, driver):
        link = "https://beta.syncwise360.com/login"
        self.login_page = LoginPage(driver, link)  # инициализируем
        self.login_page.open()                     # открываем страницу
        self.login_page.enter_user_to_site()       # входим на сайт
        time.sleep(10)

        self.course_map_page = CourseMapPage(driver, driver.current_url)
        self.course_map_page.check_incoming_message()
        time.sleep(10)

    @pytest.mark.device
    @pytest.mark.parametrize('number_of_message', list(range(1, 9)))
    def test_second(self, appium_driver, driver, number_of_message):
        self.screen = MainScreen(appium_driver)
        self.screen.press_button_menu()

        self.menu_screen = MenuScreen(appium_driver)
        self.menu_screen.press_button_send_message()

        self.send_message_screen = SendMessageScreen(appium_driver)
        self.send_message_screen.send_message(number_of_message)
        self.send_message_screen.confirm_of_message_sending()

        self.menu_screen.press_button_play_golf()

        # Запускаем
        self.course_map_page = CourseMapPage(driver, driver.current_url)
        self.course_map_page.check_incoming_message()

        time.sleep(3)

