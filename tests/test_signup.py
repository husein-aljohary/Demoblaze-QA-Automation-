# tests/test_signup.py
import pytest
import time
from pages.signup_page import SignupPage

#this test is passed one time because the user name will saved in the site
def test_signup_success(browser):
    signup_page = SignupPage(browser)
    browser.get("https://www.demoblaze.com/")
    signup_page.open_signup_modal()
    username = "user_test1231234"
    password = "test123"
    signup_page.sign_up(username, password)
    alert_text = signup_page.get_alert_text()
    assert alert_text == "Sign up successful."
    time.sleep(3)
