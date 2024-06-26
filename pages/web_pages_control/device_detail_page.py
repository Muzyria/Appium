import random

from pages.base_page import BasePage
from locators.web_locators_control import DeviceDetailPageLocators


class DeviceDetailPage(BasePage):
    def click_button_edit_ota_version(self):
        button = self.visibility_of_element_located(DeviceDetailPageLocators.BUTTON_EDIT_OTA_VERSION)
        button.click()

    def open_list_gps_version(self):
        gps_list = self.visibility_of_element_located(DeviceDetailPageLocators.LIST_GPS_VERSION)
        gps_list.click()

    def select_another_gps_version_ota(self, device_gps_version: str):
        current_version_gps = device_gps_version.replace(" ", "")
        another_gps_version = ""
        # Список пар значений
        pairs = [
            ('LC79DANR01A06S_BETA0322', 'LC79DANR01A07S'),
            ('LC79HALNR11A01S', 'LC79HALNR11A02S'),
            ('UDR1.00', 'UDR1.31')
        ]

        for pair in pairs:
            if current_version_gps in pair:
                index = pair.index(current_version_gps)
                another_gps_version = pair[1 - index]
                print(f"will select {another_gps_version}")

        row_gps_version = self.visibility_of_element_located(DeviceDetailPageLocators.SELECT_GPS_VERSION_OTA(another_gps_version))
        print(f'another GPS  - {another_gps_version}')
        row_gps_version.click()
        return another_gps_version

    def select_gps_version_for_crush(self, device_gps_version: str):
        current_version_gps = device_gps_version.replace(" ", "")
        another_gps_version = ""
        # Список пар значений
        pairs = ['LC79DANR01A06S', 'LC79DANR01A07S', 'LC79HALNR11A01S', 'LC79HALNR11A02S', 'UDR1.00', 'UDR1.31']
        # pairs = ['LC79HALNR11A01S', 'LC79HALNR11A02S', 'UDR1.00', 'UDR1.31']
        # pairs.pop(pairs.index(device_gps_version))

        another_gps_version = random.choice(pairs)
        print(f"will be selected {another_gps_version}")

        row_gps_version = self.visibility_of_element_located(DeviceDetailPageLocators.SELECT_GPS_VERSION_OTA(another_gps_version))
        print(f'another GPS  - {another_gps_version}')
        row_gps_version.click()
        return another_gps_version

    def click_button_save_ota(self):
        button_save = self.visibility_of_element_located(DeviceDetailPageLocators.BUTTON_SAVE_OTA)
        button_save.click()

    def check_gps_fw_info(self, device_gps_fw):
        """CHECK version GPS on device and reported version to web"""
        gps_fw = self.visibility_of_element_located(DeviceDetailPageLocators.DEVICE_GPS_FW).text
        assert device_gps_fw == gps_fw, f"Device FW {device_gps_fw} is not math to web control info {gps_fw}"
        print(f"Gps version on web CONTROL is {gps_fw}")

    def read_gps_fw_info(self):
        """READ version GPS on device and reported version to web"""
        return self.visibility_of_element_located(DeviceDetailPageLocators.DEVICE_GPS_FW).text
