import time

from pages.base_page import BasePage
from pages.sel_steps_page import ControlSyncWiseSteps


class TestControlSyncWise:
    class TestSelFirst:
        def test(self, selenium_driver):
            page_control = ControlSyncWiseSteps(selenium_driver, 'https://control.syncwise360.com/#login')
            page_control.open()
            time.sleep(3)
            print('Start test')
            page_control.login_page_enter_control()
            page_control.search_course("Superior")
            page_control.click_device_in_manage_device("S10150000211018049")

            page_control.choose_ota_version_update('2.1.71')

            time.sleep(10)

    class TestSelSecond:
        def test_2(self, selenium_driver):
            page_control = ControlSyncWiseSteps(selenium_driver, 'https://syncwise360.com/#login')
            page_control.open()
            time.sleep(3)
