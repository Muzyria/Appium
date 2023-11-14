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

        # def test_click_flag(self, appium_driver):
        #     el = Page(appium_driver)
        #     el.click_flag()
        #
        # def test_swipe(self, appium_driver):
        #     el = Page(appium_driver)
        #     el.swipe_my_down()
        #
        # def test_swipe_up(self, appium_driver):
        #     el = Page(appium_driver)
        #     el.swipe_my_up()
        #
        # def test_press_key(self, appium_driver):
        #     el = Page(appium_driver)
        #
        #     # el.press_key(3)
        #     el.long_press_key(26)
        #     time.sleep(5)
        #
        # def test_inter_android_menu(self, appium_driver):
        #     el = Page(appium_driver)
        #     el.android_menu()
        #
        #     el.go_to_restart()
        #
        # def test_try_make_screenshot(self, appium_driver):
        #     el = Page(appium_driver)
        #     el.try_make_screenshot()
        #
        # def test_try_make_element_screenshot(self, appium_driver):
        #     el = Page(appium_driver)
        #     el.try_make_element_screenshot()
        #
        # def test_try_check_element_visible(self, appium_driver):
        #     el = Page(appium_driver)
        #     el.try_check_visible_element()
        #
        # def test_enter_settings_yamatrak(self, appium_driver):
        #     el = Page(appium_driver)
        #     el.from_main_page_to_settings()

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



