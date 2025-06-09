# pages/login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_button_nav = (By.ID, "login2")
        self.login_username_input = (By.ID, "loginusername")
        self.login_password_input = (By.ID, "loginpassword")
        self.login_modal_button = (By.XPATH, "//button[text()='Log in']")
        self.logout_button = (By.ID, "logout2")

    def open_login_modal(self):
        self.driver.find_element(*self.login_button_nav).click()

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.login_username_input)
        )
        self.driver.find_element(*self.login_username_input).send_keys(username)
        self.driver.find_element(*self.login_password_input).send_keys(password)
        self.driver.find_element(*self.login_modal_button).click()

    def is_logged_in(self, username):
        welcome_text_locator = (By.ID, "nameofuser")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(welcome_text_locator)
        )
        welcome_text = self.driver.find_element(*welcome_text_locator).text
        return username in welcome_text

    def get_alert_text(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text