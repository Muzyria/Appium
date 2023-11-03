import base64
import os
import random
import time

import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By


from pages.base_page import BasePage
from locators.sel_elements_page_locators import ControlSyncWise

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



