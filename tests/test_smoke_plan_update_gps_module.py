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

    @pytest.fixture(scope="session", autouse=True)
    def login_to_site_360(self, driver):
        link = "https://beta.syncwise360.com/login"
        self.login_page = LoginPage360(driver, link)  # инициализируем
        self.login_page.open()  # открываем страницу
        self.login_page.enter_user_to_site()  # входим на сайт

        TestSmokeGPSModule.FIRST_TAB = self.login_page.get_window_handle()
        print(TestSmokeGPSModule.FIRST_TAB)
        time.sleep(1)

    @pytest.fixture(scope="session", autouse=True)
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

        self.login_page.switching_tab(TestSmokeGPSModule.FIRST_TAB)
        time.sleep(1)

    @pytest.mark.device
    def test_check_gps_module_version(self, appium_driver, driver):
        """
        1) Connect GPS module LC79H (GPS FW 1 - please note current FW version) to the device and confirm:
        - module detected
        - confirm GPS FW version in Asset Details Yamatrack
        - confirm GPS TYPE, GPS FW, GPS MODULE in Control Panel
        - confirm GPS FW version and GPS type in 360
        """
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
        self.GPS_MODULE_VERSION = self.asset_details_screen.look_at_gps_firmware()  # look at GPS version
        # print(self.CART_NAME)
        # print(self.DEVICE_ID)
        # print(self.GPS_MODULE_VERSION)

        # Запускаем
        self.course_map_page = CourseMapPage(driver, driver.current_url)  # инициализируем Course Map page 360
        self.course_map_page.go_to_assets_page()   # press assets button

        self.assets_page = AssetsPage(driver, driver.current_url)  # init
        self.assets_page.select_cart_in_list_by_name(self.CART_NAME)

        self.course_map_page = CourseMapPage(driver, driver.current_url)  # инициализируем Course Map page 360
        self.course_map_page.press_cart_asset_details()  # press assets details
        self.course_map_page.check_gps_version(self.GPS_MODULE_VERSION[1])  # check GPS version on 360 fnd device

        self.course_map_page.switching_tab(TestSmokeGPSModule.SECOND_TAB)  # switch to second tab

        self.control_company_page = CompanyPage(driver, driver.current_url)  # init
        self.control_company_page.select_device_by_device_id(self.DEVICE_ID)  # find and click device in list

        self.control_device_detail_page = DeviceDetailPage(driver, driver.current_url)  # init
        self.control_device_detail_page.check_gps_fw_info(self.GPS_MODULE_VERSION[1])
        time.sleep(10)

        # self.control_device_detail_page.click_button_edit_ota_version()  # click OTA edit
        # self.control_device_detail_page.open_list_gps_version()


