import time

from pages.app_steps_page import Page
from sel_test import TestControlSyncWise
from pages.adb_commands import BaseAdbCommands
from locators.app_elements_page_locators import MainScreen


class TestFirst:

    class TestAppFirst:
        adb_device = BaseAdbCommands('192.168.3.220')
        adb_device.check_devices_active()

        def test_1(self, appium_driver):
            el = Page(appium_driver)
            el.first()

        def test_a(self, appium_driver, selenium_driver):
            device = Page(appium_driver)

            # web_control = TestControlSyncWise.TestSelFirst()
            # web_control.test_choose_app(selenium_driver)
            #
            # web_syncwise = TestControlSyncWise.TestSelSecond()
            # web_syncwise.test_2(selenium_driver)

            # web_control.test_remove_app(selenium_driver)
            #
            # web_control.test_choose_app(selenium_driver)

            device.first()
            device.second()

            device.from_main_page_to_settings()
            device.third()
            device.swipe_screen_down()
            device.take_element_screenshot(MainScreen.TEXT_VIEW_APPLICATION_VERSION_APK_VALUE_ASSET_DETAILS, 'apk_version')
            apk_version = device.fourth()
            print(f'APK VERSION {apk_version}')
            assert apk_version == "2.1.77"



            # web_control.test_remove_app(selenium_driver)

            # self.adb_device.device_close_yamatack()



