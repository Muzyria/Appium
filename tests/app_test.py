import time

from pages.app_steps_page import AutomaticAPKOSUpdate
from sel_test import TestControlSyncWise
from pages.adb_commands import BaseAdbCommands
from locators.app_elements_page_locators import MainScreen

payloads_control_live = {'superior': {
    "url": "https://control.syncwise360.com/#login",
    "device_id": "S10150000211018049",
    "course_name": "Superior",
    "main_apk_version": "2.1.95",
    "update_apk_version": "2.1.71",
    "main_os_version": "2.14.3_E",
    "update_os_version": "2.12.0"
}
}

payloads_control_dev = {'superior': {
    "url": "https://dev-control.syncwise360.com/#login",
    "device_id": "S10150000211018049",
    "course_name": "Superior test ",
    "main_apk_version": "2.1.95",
    "update_apk_version": "2.1.71",
    "main_os_version": "2.14.3_E",
    "update_os_version": "2.12.0"
}
}

payloads_syncwise_dev = {'superior': {
    "url": "https://dev.syncwise360.com/#login",
    "device_id": "S10150000211018049",
    "device_name": "49",
    "main_apk_version": "2.1.95",
    "update_apk_version": "2.1.71",
    "main_os_version": "2.14.3_E",
    "update_os_version": "2.12.0"
}
}

class TestFirst:
    class TestAppFirst:
        # adb_device = BaseAdbCommands('192.168.3.220')
        # adb_device.check_devices_active()

        def test_case_one(self,  selenium_driver):
            # device = AutomaticAPKOSUpdate(appium_driver)

            # web_control = TestControlSyncWise.TestSelFirst(**payloads_control_dev['superior'])
            # web_control.test_choose_app(selenium_driver)

            web_syncwise = TestControlSyncWise.TestSelSecond(**payloads_syncwise_dev['superior'])
            web_syncwise.test_check_assets_details(selenium_driver)

            # web_control.test_remove_app(selenium_driver)
            #
            # web_control.test_choose_app(selenium_driver)

            # apk_version = device.case_one_steps()
            # print(f'APK VERSION {apk_version}')
            # assert apk_version == "2.1.77"

            # web_control.test_remove_app(selenium_driver)

            # self.adb_device.device_close_yamatack()
