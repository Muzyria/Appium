from selenium.webdriver.common.by import By


class ControlSyncWise:
    """Login Page"""
    USER_NAME = (By.XPATH, '//input[@id="username"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')
    BUTTON_LOGIN = (By.XPATH, '//button[@id="btn-submit"]')






    # def login(self):
    #     user_name = self.driver.find_element(By.XPATH, '//input[@id="username"]')  # id XPATH
    #     user_name.send_keys('superadmin')
    #     print('Input Login')
    #
    #     password = self.driver.find_element(By.XPATH, '//input[@id="password"]')  # id XPATH
    #     password.send_keys('superadmin')
    #     print('Input Password')
    #
    #     button_login = self.driver.find_element(By.XPATH, '//button[@id="btn-submit"]')  # id XPATH
    #     button_login.click()
    #     print('Click Login Button')
    #
    #     time.sleep(2)
    #
    # def search(self, data):
    #     input_search = self.driver.find_element(By.XPATH, '//input[@class="search"]')
    #     input_search.send_keys(data)
    #     input_search.send_keys(Keys.RETURN)
    #     print(f'input search --- {data}')
    #     time.sleep(1)
    #
    #     result_salt = self.driver.find_element(By.XPATH, '//*[text()="MGI Golf"]')
    #     result_salt.click()
    #     print('Click result')
    #     time.sleep(1)

