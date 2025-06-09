import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage

def test_buy_with_fully_details(browser):
    browser.get("https://www.demoblaze.com/")
    login_page = LoginPage(browser)
    login_page.open_login_modal()
    login_page.login("user_test123123", "test123")
    time.sleep(3)
    products_page = ProductsPage(browser)
    products_page.click_first_product()
    time.sleep(2)
    products_page.click_add_to_cart()
    time.sleep(2)
    alert = browser.switch_to.alert
    assert "Product added" in alert.text
    alert.accept()
    products_page.go_to_cart()
    time.sleep(2)
    cart_page = CartPage(browser)
    cart_page.click_place_order()
    time.sleep(2)
    cart_page.fill_purchase_form("Hussein", "Israel", "Tel Aviv", "123456789", "06", "2025")
    cart_page.confirm_purchase()
    confirmation = cart_page.get_confirmation_text()
    assert "Thank you for your purchase!" in confirmation
    cart_page.click_ok_on_confirmation()

#it should to fail because the details should not be empty
def test_buy_with_empty_details(browser):
    browser.get("https://www.demoblaze.com/")
    login_page = LoginPage(browser)
    login_page.open_login_modal()
    login_page.login("user_test123123", "test123")
    time.sleep(3)
    products_page = ProductsPage(browser)
    products_page.click_first_product()
    time.sleep(2)
    products_page.click_add_to_cart()
    time.sleep(2)
    alert = browser.switch_to.alert
    assert "Product added" in alert.text
    alert.accept()
    products_page.go_to_cart()
    time.sleep(2)
    cart_page = CartPage(browser)
    cart_page.click_place_order()
    time.sleep(2)
    cart_page.fill_purchase_form(" ", " ", " ", " ", " ", " ")
    cart_page.confirm_purchase()
    confirmation = cart_page.get_confirmation_text()
    assert "Thank you for your purchase!" in confirmation
    cart_page.click_ok_on_confirmation()

#this test should fail but passes (it's a bug)
def test_buy_without_login(browser):
    wait = WebDriverWait(browser, 10)
    browser.get("https://www.demoblaze.com/")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".card-title")))
    products_page = ProductsPage(browser)
    products_page.click_first_product()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']")))
    products_page.click_add_to_cart()
    wait.until(EC.alert_is_present())
    alert = browser.switch_to.alert
    assert "Product added" in alert.text
    alert.accept()
    products_page.go_to_cart()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
    cart_page = CartPage(browser)
    cart_page.click_place_order()
    wait.until(EC.visibility_of_element_located((By.ID, "orderModal")))
    cart_page.fill_purchase_form("Husein", "Israel", "Tel Aviv", "123456789", "06", "2025")
    cart_page.confirm_purchase()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "sweet-alert")))
    confirmation = cart_page.get_confirmation_text()
    assert "Thank you for your purchase!" in confirmation
    cart_page.click_ok_on_confirmation()