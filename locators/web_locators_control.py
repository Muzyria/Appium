from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_USERNAME = (By.CSS_SELECTOR, "input#username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input#password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button#btn-submit")


class CompanyPageLocators:
    @staticmethod
    def DEVICE_IN_DEVICE_LIST(device_id):
        return (By.XPATH, f"//*[text()='{device_id}']")


class DeviceDetailPageLocators:
    BUTTON_EDIT_OTA_VERSION = (By.XPATH, "//div[contains(text(), 'OTA')]/following-sibling::div[@class='bt edit']")
    LIST_GPS_VERSION = (By.CSS_SELECTOR, "select[name='gpsVersion']")

    DEVICE_GPS_FW = (By.CSS_SELECTOR, 'div:nth-child(6) > div.content > div:nth-child(2) > div:nth-child(10) > div.desc')
