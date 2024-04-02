import time
import pytest

from pages.web_pages_360.login_page_360 import LoginPage360
from pages.web_pages_360.course_map_page import CourseMapPage
from pages.web_pages_360.assets_page import AssetsPage

from pages.web_pages_control.login_page_control import LoginPageControl
from pages.web_pages_control.company_page import CompanyPage
from pages.web_pages_control.device_detail_page import DeviceDetailPage

from pages.device_pages.main_screen import MainScreen
from pages.device_pages.menu_screen import MenuScreen
from pages.device_pages.settings_screen import SettingsScreen
from pages.device_pages.asset_details_screen import AssetDetailsScreen


"""
2) Change in Control Panel GPS FW version GPS module LC79H from FW 1 to from FW 2 note FW version)
- Confirm if GPS module LC79H updated successfuly
- module detected
- confirm GPS FW version in Asset Details Yamatrack
- confirm GPS TYPE, GPS FW, GPS MODULE in Control Panel
- confirm GPS FW version and GPS type in 360

3) after step 2 - Change in Control Panel GPS FW version GPS module LC79H to LC79D
- try update module and confirm if update is not available - Expected

4) after step 3 - Change in Control Panel GPS FW version GPS module LC79D to Ublox
- try update module and confirm if update is not available - Expected
"""


class TestSmokeGPSModule:
    CART_NAME = ""
    DEVICE_ID = ""
    GPS_MODULE_VERSION = ""
    FIRST_TAB = None
    SECOND_TAB = None

    @pytest.fixture(scope="function", autouse=True)
    def login_to_site_360(self, driver):
        link = "https://beta.syncwise360.com/login"
        self.login_page = LoginPage360(driver, link)  # инициализируем
        self.login_page.open()  # открываем страницу
        self.login_page.enter_user_to_site()  # входим на сайт

        TestSmokeGPSModule.FIRST_TAB = self.login_page.get_window_handle()
        print(TestSmokeGPSModule.FIRST_TAB)
        time.sleep(1)

    @pytest.fixture(scope="function", autouse=True)
    def login_to_site_control(self, driver):
        self.login_page.switch_to_new_tab()
        TestSmokeGPSModule.SECOND_TAB = self.login_page.get_window_handle()
        print(TestSmokeGPSModule.SECOND_TAB)

        link = "https://control.syncwise360.com/#company/4442"
        self.login_page = LoginPageControl(driver, link)  # инициализируем
        self.login_page.open()  # открываем страницу
        self.login_page.enter_user_to_site()  # входим на сайт
        time.sleep(2)
        self.login_page.open_new_url(link)
        time.sleep(1)

        self.login_page.switching_tab(TestSmokeGPSModule.FIRST_TAB)  # switch to FIRST_TAB
        time.sleep(1)

    def run_web_checks(self, driver):
        # Запускаем WEB
        self.course_map_page = CourseMapPage(driver, driver.current_url)  # инициализируем Course Map page 360
        self.course_map_page.go_to_assets_page()  # press assets button

        self.assets_page = AssetsPage(driver, driver.current_url)  # init
        self.assets_page.select_cart_in_list_by_name(self.CART_NAME)

        self.course_map_page = CourseMapPage(driver, driver.current_url)  # инициализируем Course Map page 360
        self.course_map_page.press_cart_asset_details()  # press assets details
        self.course_map_page.check_gps_version(self.GPS_MODULE_VERSION)  # check GPS version on 360 fnd device

        self.course_map_page.switching_tab(TestSmokeGPSModule.SECOND_TAB)  # switch to SECOND_TAB

        self.control_company_page = CompanyPage(driver, driver.current_url)  # init
        self.control_company_page.select_device_by_device_id(self.DEVICE_ID)  # find and click device in list

        self.control_device_detail_page = DeviceDetailPage(driver, driver.current_url)  # init
        self.control_device_detail_page.check_gps_fw_info(self.GPS_MODULE_VERSION)  # check gps version in control

        self.control_company_page.switching_tab(self.FIRST_TAB)   # switch to FIRST_TAB
        time.sleep(5)

    def run_web_select_gps_version_update(self, driver):
        # Запускаем WEB
        self.course_map_page = CourseMapPage(driver, driver.current_url)  # инициализируем Course Map page 360
        self.course_map_page.switching_tab(self.SECOND_TAB)  # switch to SECOND_TAB

        self.control_company_page = CompanyPage(driver, driver.current_url)  # init
        self.control_company_page.select_device_by_device_id(self.DEVICE_ID)  # find and click device in list

        self.control_device_detail_page = DeviceDetailPage(driver, driver.current_url)  # init
        self.control_device_detail_page.click_button_edit_ota_version()  # click OTA edit
        self.control_device_detail_page.open_list_gps_version()
        self.control_device_detail_page.select_another_gps_version_ota(self.GPS_MODULE_VERSION)   # select another version
        self.control_device_detail_page.click_button_save_ota()  # click button SAVE OTA
        time.sleep(5)
        self.control_device_detail_page.refresh_tab()
        self.control_company_page.switching_tab(self.FIRST_TAB)  # switch to FIRST_TAB

    def get_device_info(self, appium_driver):
        self.screen = MainScreen(appium_driver)  # инициализируем Main screen
        self.screen.press_button_menu()  # Press button menu

        self.menu_screen = MenuScreen(appium_driver)  # инициализируем Menu screen
        self.menu_screen.press_button_settings()  # Press button settings

        self.settings_screen = SettingsScreen(appium_driver)  # init
        self.settings_screen.enter_password()  # enter password
        self.settings_screen.press_asset_details_button()  # press asset details

        self.asset_details_screen = AssetDetailsScreen(appium_driver)  # init
        self.CART_NAME = self.asset_details_screen.get_cart_name()
        self.DEVICE_ID = self.asset_details_screen.get_device_id()
        self.GPS_MODULE_VERSION = self.asset_details_screen.look_at_gps_firmware()[1]  # look at GPS version
        print(self.CART_NAME)
        print(self.DEVICE_ID)
        print(self.GPS_MODULE_VERSION)

        self.asset_details_screen.press_button_cancel()  # return to play golf
        self.settings_screen.press_button_cancel()
        self.menu_screen.press_button_play_golf()

    def full_app_reset(self, appium_driver):
        self.screen = MainScreen(appium_driver)  # инициализируем Main screen
        self.screen.press_button_menu()  # Press button menu

        self.menu_screen = MenuScreen(appium_driver)  # инициализируем Menu screen
        self.menu_screen.press_button_settings()  # Press button settings

        self.settings_screen = SettingsScreen(appium_driver)  # init
        self.settings_screen.enter_password()  # enter password

        self.settings_screen.press_full_app_reset_button()  # press full app reset button
        self.settings_screen.press_yes_button()  # press YES button

    @pytest.mark.skip
    @pytest.mark.device
    def test_check_gps_module_version(self, appium_driver, driver):
        """
        1) Connect GPS module LC79H (GPS FW 1 - please note current FW version) to the device and confirm:
        - module detected
        - confirm GPS FW version in Asset Details Yamatrack
        - confirm GPS TYPE, GPS FW, GPS MODULE in Control Panel
        - confirm GPS FW version and GPS type in 360
        """
        #RUN DEVICE
        self.get_device_info(appium_driver)

        # RUN WEB
        self.run_web_checks(driver)

    @pytest.mark.device
    def test_check_gps_module_version_after_update(self, appium_driver, driver):
        """
        2) Change in Control Panel GPS FW version GPS module LC79H from FW 1 to from FW 2 note FW version)
        - Confirm if GPS module LC79H updated successfuly
        - module detected
        - confirm GPS FW version in Asset Details Yamatrack
        - confirm GPS TYPE, GPS FW, GPS MODULE in Control Panel
        - confirm GPS FW version and GPS type in 360
        """

        self.get_device_info(appium_driver)
        self.run_web_select_gps_version_update(driver)
        time.sleep(5)
        self.full_app_reset(appium_driver)

        self.screen = MainScreen(appium_driver)  # инициализируем Main screen
        self.screen.wait_button_menu(200)  # WAIT BUTTON MENU
        print("--START_CHECKS__")

        time.sleep(5)
        self.get_device_info(appium_driver)
        self.run_web_checks(driver)
        time.sleep(20)
