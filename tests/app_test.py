
from pages.app_steps_page import Page


class TestFirst:
    class TestAppFiras:

        def test_1(self, appium_driver):
            el = Page(appium_driver)
            el.first()

        def test_click_flag(self, appium_driver):
            el = Page(appium_driver)
            el.click_flag()

