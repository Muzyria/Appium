import time

from pages.app_steps_page import Page


class TestFirst:
    class TestAppFiras:

        def test_1(self, appium_driver):
            el = Page(appium_driver)
            el.first()

        def test_click_flag(self, appium_driver):
            el = Page(appium_driver)
            el.click_flag()

        def test_swipe(self, appium_driver):
            el = Page(appium_driver)
            el.swipe_my_down()

        def test_swipe_up(self, appium_driver):
            el = Page(appium_driver)
            el.swipe_my_up()

        def test_press_key(self, appium_driver):
            el = Page(appium_driver)

            # el.press_key(3)
            el.long_press_key(26)
            time.sleep(5)

        def test_inter_android_menu(self, appium_driver):
            el = Page(appium_driver)
            el.android_menu()

            el.go_to_restart()

        def test_try_make_screenshot(self, appium_driver):
            el = Page(appium_driver)
            el.try_make_screenshot()

        def test_try_make_element_screenshot(self, appium_driver):
            el = Page(appium_driver)
            el.try_make_element_screenshot()

