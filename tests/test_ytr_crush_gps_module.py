import time
import pytest

from pages.web_pages_control.company_page import CompanyPage
from pages.web_pages_control.device_detail_page import DeviceDetailPage
from pages.web_pages_control.login_page_control import LoginPageControl
from pages.base_page import AdbCommands

class TestGPSUpdate:
    # CART_NAME = "49_E"
    CART_NAME = "A5"
    # DEVICE_ID = "E10150000211018049"
    DEVICE_ID = "L101140017180605A5"
    CURRENT_GPS_MODULE_VERSION = "LC79DANR01A06S_BETA0322"
    ALTERNATIVE_GPS_MODULE_VERSION = "LC79DANR01A07S"
    UPDATE_GPS_MODULE_VERSION = ""

    @pytest.fixture(scope="function", autouse=True)
    def login_to_site_control(self, driver):
        link = "https://control.syncwise360.com/#company/4442"
        self.login_page = LoginPageControl(driver, link)  # инициализируем
        self.login_page.open()  # открываем страницу
        self.login_page.enter_user_to_site()  # входим на сайт
        time.sleep(2)
        self.login_page.open_new_url(link)
        # time.sleep(3)

    @pytest.fixture(scope="function", autouse=True)
    def connect_device(self):
        print(f"ADB FIXTURE")
        self.ip_device = "192.168.0.102"
        self.adb_command = AdbCommands(self.ip_device)
        print(f"Connect device {self.ip_device}")
        self.adb_command.device_connect()

    def run_web_checks(self, driver):
        """Запускаем WEB и проверяем версию прошивки GPS котрую отправляет планшет на сайт"""
        self.control_company_page = CompanyPage(driver, driver.current_url)  # init
        self.control_company_page.select_device_by_device_id(self.DEVICE_ID)  # find and click device in list
        gps_version = self.control_device_detail_page.read_gps_fw_info()  # read gps version in control
        print()
        print(f"version on site is -------------------- {gps_version}")
        assert gps_version not in ['LC79DANR01A06S', 'LC79DANR01A07S', 'LC79HALNR11A01S', 'LC79HALNR11A02S', 'UDR1.00', 'UDR1.31']
        print()

    def run_web_select_gps_version_update(self, driver):
        # Запускаем WEB и выбираем версиию для обновления GPS
        self.control_company_page = CompanyPage(driver, driver.current_url)  # init
        self.control_company_page.select_device_by_device_id(self.DEVICE_ID)  # find and click device in list

        self.control_device_detail_page = DeviceDetailPage(driver, driver.current_url)  # init
        self.control_device_detail_page.click_button_edit_ota_version()  # click OTA edit
        self.control_device_detail_page.open_list_gps_version()

        self.UPDATE_GPS_MODULE_VERSION = self.control_device_detail_page.select_gps_version_for_crush(self.CURRENT_GPS_MODULE_VERSION)   # select another version
        print(f"FOR UPDATE GPS VERSION - {self.UPDATE_GPS_MODULE_VERSION}")
        self.control_device_detail_page.click_button_save_ota()  # click button SAVE OTA
        time.sleep(5)
        self.control_device_detail_page.refresh_tab()
        time.sleep(3)

    def run_device_sync(self):
        self.adb_command.touch_screen()
        self.adb_command.device_in_off_hole()
        self.adb_command.touch_screen()

    @pytest.mark.parametrize("i", range(1, 100))
    def test_try_to_crush_gps(self, driver, i):
        """
        Will make a lot of update firmware  gps module
        """
        print(f"Running test {i}")
        self.run_web_select_gps_version_update(driver)
        time.sleep(5)

        self.run_device_sync()
        time.sleep(90)

        self.run_web_checks(driver)
        time.sleep(5)

