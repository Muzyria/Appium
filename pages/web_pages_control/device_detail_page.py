from pages.base_page import BasePage
from locators.web_locators_control import DeviceDetailPageLocators


class DeviceDetailPage(BasePage):
    def click_button_edit_ota_version(self):
        button = self.element_is_visible(DeviceDetailPageLocators.BUTTON_EDIT_OTA_VERSION)
        button.click()

    def open_list_gps_version(self):
        gps_list = self.element_is_visible(DeviceDetailPageLocators.LIST_GPS_VERSION)
        gps_list.click()

    def check_gps_fw_info(self, device_gps_fw):
        gps_fw = self.element_is_visible(DeviceDetailPageLocators.DEVICE_GPS_FW).text
        assert device_gps_fw == gps_fw, f"Device FW {device_gps_fw} is not math to web control info {gps_fw}"
