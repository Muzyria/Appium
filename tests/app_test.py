import time

from pages.app_steps_page import Page
from sel_test import TestControlSyncWise
from pages.adb_commands import BaseAdbCommands


class TestFirst:

    class TestAppFirst:
        adb_device = BaseAdbCommands('192.168.3.219')
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
            # device = Page(appium_driver)
            # device.first()

            web_control = TestControlSyncWise.TestSelFirst()
            web_control.test(selenium_driver)


            web_syncwise = TestControlSyncWise.TestSelSecond()
            web_syncwise.test_2(selenium_driver)

            # device.second()

            web_control.test(selenium_driver)

            # device.from_main_page_to_settings()

            self.adb_device.device_close_yamatack()

