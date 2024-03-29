import time
import pytest

from pages.web_pages.login_page import LoginPage
from pages.web_pages.course_map_page import CourseMapPage

from pages.device_pages.main_screen import MainScreen
from pages.device_pages.menu_screen import MenuScreen
from pages.device_pages.send_massage_screen import SendMessageScreen
from pages.device_pages.select_language_page import SelectLanguageScreen


class TestSendMessages:

    @pytest.fixture(scope="session", autouse=True)
    def login_to_site(self, driver):
        link = "https://beta.syncwise360.com/login"
        self.login_page = LoginPage(driver, link)  # инициализируем
        self.login_page.open()  # открываем страницу
        self.login_page.enter_user_to_site()  # входим на сайт
        time.sleep(10)

    @pytest.mark.skip
    @pytest.mark.parametrize('number_of_language', list(range(1, 9)))
    def test_device_select_language(self, appium_driver, number_of_language):
        self.screen = MainScreen(appium_driver)                         # инициализируем Main screen
        self.screen.press_button_select_language()                      # press button select language

        self.language_screen = SelectLanguageScreen(appium_driver)      # инициализируем Select Language screen
        self.language_screen.select_language(number_of_language)        # press button language
        time.sleep(1)
        yield self

    @pytest.mark.device
    @pytest.mark.parametrize('number_of_message', list(range(1, 3)))
    def test_send_device_message(self, appium_driver, driver, number_of_message):
        self.screen = MainScreen(appium_driver)                         # инициализируем Main screen
        self.screen.press_button_menu()                                 # Press button menu

        self.menu_screen = MenuScreen(appium_driver)                    # инициализируем Menu screen
        self.menu_screen.press_button_send_message()                    # press button message

        self.send_message_screen = SendMessageScreen(appium_driver)     # инициализируем Send message screen
        self.send_message_screen.send_message(number_of_message)        # press message
        self.send_message_screen.confirm_of_message_sending()           # press button Yes

        self.menu_screen.press_button_play_golf()                       # press button Play Golf

        # Запускаем
        self.course_map_page = CourseMapPage(driver, driver.current_url)  # инициализируем Course Map page
        self.course_map_page.check_incoming_message()                     # wait and press confirm message
        time.sleep(3)
