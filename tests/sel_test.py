import time

from pages.base_page import BasePage
from pages.sel_steps_page import ControlSyncWiseSteps, SyncWiseSteps


class TestControlSyncWise:
    class TestSelFirst:
        def __init__(self, url, device_id, course_name, main_apk_version, update_apk_version, main_os_version,
                     update_os_version):
            self.url = url
            self.device_id = device_id
            self.course_name = course_name
            self.main_apk_version = main_apk_version
            self.update_apk_version = update_apk_version
            self.main_os_version = main_os_version
            self.update_os_version = update_os_version

        def test_choose_app(self, selenium_driver):
            page_control = ControlSyncWiseSteps(selenium_driver, self.url)
            page_control.open()
            time.sleep(3)
            print('Start test')
            page_control.login_page_enter_control()
            page_control.search_course(self.course_name)
            page_control.click_device_in_manage_device(self.device_id)
            time.sleep(3)
            page_control.choose_ota_version_update(self.update_apk_version)
            time.sleep(2)
            page_control.web_control_log_out()

        def test_remove_app(self, selenium_driver):
            page_control = ControlSyncWiseSteps(selenium_driver, self.url)
            page_control.open()
            time.sleep(3)
            print('Start test')
            page_control.login_page_enter_control()
            page_control.search_course(self.course_name)
            page_control.click_device_in_manage_device(self.device_id)
            time.sleep(3)
            page_control.choose_ota_version_press_button_edit()
            print('Click Button Edit OTA')

            page_control.web_control_remove_app_update()
            time.sleep(2)
            page_control.web_control_log_out()

    class TestSelSecond:
        def __init__(self, url, device_id, device_name, main_apk_version, update_apk_version, main_os_version,
                     update_os_version):
            self.url = url
            self.device_id = device_id
            self.device_name = device_name
            self.main_apk_version = main_apk_version
            self.update_apk_version = update_apk_version
            self.main_os_version = main_os_version
            self.update_os_version = update_os_version

        def test_2(self, selenium_driver):
            page_syncwice = SyncWiseSteps(selenium_driver, self.url)
            page_syncwice.open()
            time.sleep(5)
            page_syncwice.login_page_enter_syncwise()
            time.sleep(5)
            page_syncwice.choose_assert_device_name()
            time.sleep(10)

