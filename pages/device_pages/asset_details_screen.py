from pages.base_page import AppiumBasePage
from locators.android_locators import AssetDetailsLocators


class AssetDetailsScreen(AppiumBasePage):
    def look_at_gps_firmware(self):
        self.swipe_screen_down()
        self.swipe_screen_down()
        key = self.element_is_visible(AssetDetailsLocators.SELECT_ASSET_DETAILS_KEY_BY_NUMBER(6))
        value = self.element_is_visible(AssetDetailsLocators.SELECT_ASSET_DETAILS_VALUE_BY_NUMBER(6))
        # print(key.text)
        # print(value.text)
        return key.text, value.text

    def get_device_id(self):
        device_id = self.element_is_visible(AssetDetailsLocators.DEVICE_ID)
        return device_id.text

    def get_cart_name(self):
        cart_name = self.element_is_visible(AssetDetailsLocators.CART_NAME)
        return cart_name.text

