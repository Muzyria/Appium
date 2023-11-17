import base64
import os
import random
import time

import requests
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.sel_elements_page_locators import ControlSyncWise, SyncWise

from selenium.webdriver import Keys


class ControlSyncWiseSteps(BasePage):
    locators = ControlSyncWise()

    def login_page_enter_control(self):
        self.element_is_visible(self.locators.USER_NAME).send_keys('superadmin')
        print("Input LOGIN")
        self.element_is_visible(self.locators.PASSWORD).send_keys('superadmin')
        print("Input PASSWORD")
        self.element_is_visible(self.locators.BUTTON_LOGIN).click()
        print("Click BUTTON LOG IN")



    def search_course(self, data_search):
        input_search = self.element_is_visible(self.locators.FIELD_SEARCH)
        input_search.send_keys(data_search)
        input_search.send_keys(Keys.RETURN)
        print(f'Input search --- {data_search}')
        # time.sleep(1)
        self.element_is_visible(self.locators.find_by_text(data_search)).click()
        print('Click result')
        time.sleep(2)

    def click_device_in_manage_device(self, id_device):
        # self.element_is_visible(self.locators.BUTTON_MANAGE_DEVICE).click()
        self.element_is_visible(self.locators.find_by_text('Manage Devices')).click()
        print('Click Manage Device')
        self.element_is_visible(self.locators.find_by_text(id_device)).click()
        print(f'Click Device {id_device}')
        time.sleep(2)

    def choose_ota_version_press_button_edit(self, app_version=None, os_version=None):
        self.element_is_visible(self.locators.OTA_VERSION_BUTTON_EDIT).click()
        print('Click Button Edit OTA')

    def choose_ota_version_update(self, app_version=None, os_version=None):
        self.element_is_visible(self.locators.OTA_VERSION_BUTTON_EDIT).click()
        print('Click Button Edit OTA')

        self.element_is_visible(self.locators.app_version(app_version)).click()
        print(f'Selected APK Version {app_version}')

        self.element_is_visible(self.locators.OTA_VERSION_BUTTON_SAVE).click()
        print('Press Button Save')

        time.sleep(5)

    def web_control_remove_app_update(self):
        self.element_is_visible(self.locators.BUTTON_REMOVE_APP_UPDATE).click()

    def web_control_remove_os_update(self):
        self.element_is_visible(self.locators.BUTTON_REMOVE_APP_UPDATE).click()

    def web_control_log_out(self):
        self.element_is_visible(self.locators.BUTTON_LOG_OUT).click()
        print("Button Log Out Press")


class SyncWiseSteps(BasePage):
    locators = SyncWise()

    def login_page_enter_syncwise(self):
        self.element_is_visible(self.locators.USER_NAME).send_keys('QA')
        print("Input LOGIN")
        self.element_is_visible(self.locators.PASSWORD).send_keys('Qwerty01!')
        print("Input PASSWORD")
        self.element_is_visible(self.locators.BUTTON_LOGIN).click()
        print("Click BUTTON LOG IN")

    def choose_assert_device_name(self):
        self.element_is_visible(self.locators.BUTTON_ASSERT).click()
        print("Click BUTTON ASSERT")
        self.element_is_visible(self.locators.find_by_text('49')).click()

    def asset_details_values(self):
        # self.scroll_element_by_mouse(self.element_is_visible(self.locators.ASSET_DETAILS_LIST))
        self.go_to_element(self.element_is_visible(self.locators.ASSET_DETAILS_APK_VERSION))

        # try:
        #     cable_voltage = self.element_is_visible(self.locators.ASSET_DETAILS_CABLE_VOLTAGE).text
        # except TimeoutException:
        #     cable_voltage = None

        os_fw = self.element_is_visible(self.locators.ASSET_DETAILS_OS_VERSION).text
        apk_fw = self.element_is_visible(self.locators.ASSET_DETAILS_APK_VERSION).text
        cable_fw = self.element_is_visible(self.locators.ASSET_DETAILS_CABLE_FW_VERSION).text
        gps_fw = [i.text for i in self.elements_are_present(self.locators.ASSET_DETAILS_GPS_FW_VERSION)]

        return {
            # 'cable_voltage': cable_voltage,
            'os_fw': os_fw,
            'apk_fw': apk_fw,
            'cable_fw': cable_fw,
            'gps_fw': gps_fw[0] if gps_fw else None
        }
