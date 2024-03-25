import time

from pages.app_steps_page import AutomaticAPKOSUpdate

from pages.adb_commands import BaseAdbCommands




class TestFirst:
    class TestAppFirst:
        adb_device = BaseAdbCommands('192.168.0.105')
        adb_device.check_devices_active()

        def test_case_one(self,  selenium_driver, appium_driver):
            device = AutomaticAPKOSUpdate(appium_driver)

            # web_syncwise = TestControlSyncWise.TestSelSecond(**payloads_syncwise_live['superior'])
            # web_syncwise.test_check_assets_details(selenium_driver)

            # web_control = TestControlSyncWise.TestSelFirst(**payloads_control_dev['superior'])
            # web_control.test_choose_app(selenium_driver)

            # web_control.test_remove_app(selenium_driver)
            # web_control.test_choose_app(selenium_driver)

            apk_version = device.case_one_steps()
            print(f'APK VERSION {apk_version}')
            assert apk_version == "2.1.77"

            # web_control.test_remove_app(selenium_driver)

            # self.adb_device.device_close_yamatack()
