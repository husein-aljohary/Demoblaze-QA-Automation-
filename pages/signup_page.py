# pages/signup_page.py
from selenium.webdriver.common.by import By
import time

class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.signup_button = (By.ID, "signin2")
        self.username_input = (By.ID, "sign-username")
        self.password_input = (By.ID, "sign-password")
        self.submit_button = (By.XPATH, "//button[text()='Sign up']")

    def open_signup_modal(self):
        self.driver.find_element(*self.signup_button).click()
        time.sleep(2)

    def sign_up(self, username, password):
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.submit_button).click()
        time.sleep(3)

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text
