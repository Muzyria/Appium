import time

import pytest

from pages.web_pages.login_page import LoginPage
from pages.web_pages.course_map_page import CourseMapPage


@pytest.mark.device
def test_first(driver):
    link = "https://beta.syncwise360.com/login"
    login_page = LoginPage(driver, link)  # инициализируем
    login_page.open()                     # открываем страницу
    login_page.enter_user_to_site()       # входим на сайт
    time.sleep(10)

    course_map_page = CourseMapPage(driver, driver.current_url)
    course_map_page.check_incoming_message()
    time.sleep(10)


