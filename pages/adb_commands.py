import os
import subprocess
import time
from datetime import datetime, timedelta
import re


class BaseAdbCommands:
    def __init__(self, ip_device=None):
        self.ip_device = ip_device

    @staticmethod
    def device_read_ip_address():
        """Получение IP адрес девайса при подключении по USB"""
        os.system(fr'adb shell ip addr show wlan0')  # читаем IP девайса
        result = subprocess.run(["adb", "shell", "ip", "addr", "show", "wlan0"], capture_output=True, text=True)
        output_lines = result.stdout.splitlines()

        # Регулярное выражение для извлечения IP-адреса
        pattern = r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        ip_address = re.search(pattern, [item for item in output_lines if 'inet ' in item][0]).group(0).split()[1]
        print(ip_address)
        return ip_address

    def adb_get_state(self):
        output = os.system('adb get-state')
        # print(f'{output}')
        return output

    def device_disconnect(self):
        os.system(f'adb disconnect {self.ip_device}')

    def device_connect(self):
        os.system(f'adb connect {self.ip_device}')

    def device_reboot(self):
        os.system(f'adb -s {self.ip_device} reboot')

    def check_devices_active(self):
        """Проверяем, есть ли подключенные устройства в выводе в консоль"""
        output = subprocess.check_output(['adb', 'devices'])
        if self.ip_device in str(output) and "offline" not in str(output):
            print('Устройство Android подключено и активно.')

        else:
            print(f'Устройство Android {self.ip_device} будет подключено By TCP/IP')
            self.device_disconnect()
            time.sleep(2)
            self.device_connect()

    def device_in_cart_barn(self):
        os.system(f'adb -s {self.ip_device} shell am broadcast -a com.l1inc.yamatrack3d.action.powermanagement.cart_barn_sleep')

    def device_in_off_hole(self):
        os.system(f'adb -s {self.ip_device} shell am broadcast -a com.l1inc.yamatrack3d.action.powermanagement.not_on_hole_sleep')



    def device_close_yamatack(self):
        os.system(f'adb -s {self.ip_device} shell am force-stop com.l1inc.yamatrack3d')

    def device_close_all(self):
        os.system(f'adb -s {self.ip_device} shell input keyevent KEYCODE_HOME')

    def device_kill_app(self):
        os.system(f'adb -s {self.ip_device} shell input keyevent KEYCODE_APP_SWITCH')
        os.system(f'adb -s {self.ip_device} shell input keyevent DEL')

    def device_get_system_volume_speaker(self):
        """Get value system volume speaker"""
        os.system(f'adb -s {self.ip_device} shell settings get system volume_alarm_speaker')

    """SETTINGS PAGES"""
    def device_open_settings_main_page(self):
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.SETTINGS')

    def device_open_wifi_settings(self):
        """Open page Settings WI-FI"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.WIFI_SETTINGS')

    def device_open_wireless_settings(self):
        """Open page Settings WireLess"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.WIRELESS_SETTINGS')

    def device_open_sounds_settings(self):
        """Open page Settings Sounds"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.SOUND_SETTINGS')

    def device_open_location_settings(self):
        """Open page Settings Location"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.LOCATION_SOURCE_SETTINGS')

    def open_date_settings(self):
        """Open page Settings Date"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.DATE_SETTINGS')

    def open_device_info_settings(self):
        """Open page Settings Device Info"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.DEVICE_INFO_SETTINGS')

    def open_device_developer_options_settings(self):
        """Open page Settings Developer Options"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.APPLICATION_DEVELOPMENT_SETTINGS')


test = BaseAdbCommands('192.168.3.235')
# test.check_devices_active()
# test.device_reboot()
# test.device_in_off_hole()
# test.device_open_wifi_settings()
# test.device_close_all()
# test.device_close_yamatack()
# test.device_kill_app()
# test.device_read_ip_address()
test.device_connect()
# test.device_disconnect()
test.open_device_info_settings()


# def get_value_new_time(self, minutes=1, seconds=10):
#     """RETURN NEW TIME"""
#     now = datetime.now()  # получаем текущее время
#     one_minute_later = now + timedelta(minutes=minutes, seconds=seconds)  # добавляем 1 минуту к текущему времени
#     hour = one_minute_later.time().hour  # получаем часы через 1 минуту
#     minute = one_minute_later.time().minute  # получаем минуты через 1 минуту
#     print(f'Расчетное время power_off_time={hour:02}:{minute:02}')
#     print()
#     return f'{hour:02}{minute:02}'
#
# def get_time_off(self):
#     print('time_off ', end='')
#     os.system(f'adb shell settings get system power_off_time')
#
# def get_random_power_off_time(self):
#     print('random_power_off_time ', end='')
#     os.system(f'adb shell settings get system random_power_off_time')
#
# def put_time_off(self, time):
#     os.system(f'adb shell settings put system power_off_time {time}')
#
# def put_random_power_off_time(self, time):
#     os.system(f'adb shell settings put system random_power_off_time {time}')
#