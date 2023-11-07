import time

from pages.base_page import BasePage
from pages.sel_steps_page import ControlSyncWiseSteps


class TestControlSyncWise:
    class TestSelFirst:
        def test_choose_app(self, selenium_driver):
            page_control = ControlSyncWiseSteps(selenium_driver, 'https://control.syncwise360.com/#login')
            page_control.open()
            time.sleep(3)
            print('Start test')
            page_control.login_page_enter_control()
            page_control.search_course("Superior")
            page_control.click_device_in_manage_device("S10150000211018049")
            time.sleep(3)
            page_control.choose_ota_version_update('2.1.71')
            time.sleep(2)
            page_control.web_control_log_out()

        def test_remove_app(self, selenium_driver):
            page_control = ControlSyncWiseSteps(selenium_driver, 'https://control.syncwise360.com/#login')
            page_control.open()
            time.sleep(3)
            print('Start test')
            page_control.login_page_enter_control()
            page_control.search_course("Superior")
            page_control.click_device_in_manage_device("S10150000211018049")
            time.sleep(3)
            page_control.choose_ota_version_press_button_edit()
            print('Click Button Edit OTA')

            page_control.web_control_remove_app_update()
            time.sleep(2)
            page_control.web_control_log_out()

    class TestSelSecond:
        def test_2(self, selenium_driver):
            page_control = ControlSyncWiseSteps(selenium_driver, 'https://syncwise360.com/#login')
            page_control.open()
            time.sleep(3)
