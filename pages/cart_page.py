from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Place Order']")
    NAME_INPUT = (By.ID, "name")
    COUNTRY_INPUT = (By.ID, "country")
    CITY_INPUT = (By.ID, "city")
    CREDIT_CARD_INPUT = (By.ID, "card")
    MONTH_INPUT = (By.ID, "month")
    YEAR_INPUT = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//button[text()='Purchase']")
    CONFIRMATION_TEXT = (By.CLASS_NAME, "sweet-alert")
    OK_BUTTON = (By.XPATH, "//button[text()='OK']")

    def click_place_order(self):
        self.driver.find_element(*self.PLACE_ORDER_BUTTON).click()

    def fill_purchase_form(self, name, country, city, credit_card, month, year):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.COUNTRY_INPUT).send_keys(country)
        self.driver.find_element(*self.CITY_INPUT).send_keys(city)
        self.driver.find_element(*self.CREDIT_CARD_INPUT).send_keys(credit_card)
        self.driver.find_element(*self.MONTH_INPUT).send_keys(month)
        self.driver.find_element(*self.YEAR_INPUT).send_keys(year)

    def confirm_purchase(self):
        self.driver.find_element(*self.PURCHASE_BUTTON).click()

    def get_confirmation_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CONFIRMATION_TEXT)
        )
        return self.driver.find_element(*self.CONFIRMATION_TEXT).text

    def click_ok_on_confirmation(self):
        self.driver.find_element(*self.OK_BUTTON).click()
