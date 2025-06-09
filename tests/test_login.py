# tests/test_login.py
import time

import pytest
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_success(browser):
    login_page = LoginPage(browser)
    browser.get("https://www.demoblaze.com/")
    login_page.open_login_modal()
    username = "user_test1231234"
    password = "test123"
    login_page.login(username, password)
    assert login_page.is_logged_in(username)

def test_login_failure(browser):
    login_page = LoginPage(browser)
    browser.get("https://www.demoblaze.com/")
    login_page.open_login_modal()
    invalid_username = "wrong_user"
    invalid_password = "wrong"
    login_page.login(invalid_username, invalid_password)
    time.sleep(3)
    alert_text = login_page.get_alert_text()
    assert alert_text == "User does not exist."

def test_login_success_weak_password_username(browser):
    login_page = LoginPage(browser)
    browser.get("https://www.demoblaze.com/")
    login_page.open_login_modal()
    username = "0"
    password = "0"
    login_page.login(username, password)
    assert login_page.is_logged_in(username)