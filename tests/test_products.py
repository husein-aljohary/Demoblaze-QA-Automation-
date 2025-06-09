# tests/test_products.py
import time
import pytest
from selenium.webdriver.common.by import By
from pages.products_page import ProductsPage
from pages.login_page import LoginPage

def test_products_displayed(browser):
    browser.get("https://www.demoblaze.com/")
    login_page = LoginPage(browser)
    login_page.open_login_modal()
    login_page.login("user_test123123", "test123")
    time.sleep(3)
    products_page = ProductsPage(browser)
    num_products = products_page.get_number_of_products_displayed()
    assert num_products > 0, "No products are displayed on the homepage"



def test_carousel_all_indicators_change_image(browser):
    browser.get("https://www.demoblaze.com/")
    time.sleep(2)
    indicators = browser.find_elements(By.CSS_SELECTOR, "#carouselExampleIndicators ol.carousel-indicators li")
    image_sources = set()
    for index, indicator in enumerate(indicators):
        indicator.click()
        time.sleep(2)
        active_image = browser.find_element(By.CSS_SELECTOR, "#carouselExampleIndicators .carousel-item.active img")
        src = active_image.get_attribute("src")
        image_sources.add(src)
    assert len(image_sources) == len(indicators), f"Number of photos ({len(image_sources)}) the number of points does not match ({len(indicators)})"

def test_click_product_opens_details(browser):
    browser.get("https://www.demoblaze.com/")
    login_page = LoginPage(browser)
    login_page.open_login_modal()
    login_page.login("user_test123123", "test123")
    time.sleep(3)
    products_page = ProductsPage(browser)
    product_titles = products_page.get_all_product_titles()
    first_product_name = product_titles[0]
    products_page.click_first_product()
    time.sleep(2)
    detail_title = products_page.get_product_title_on_details_page()
    assert first_product_name == detail_title, "Product name does not match on detail page"

def test_click_product_opens_details_from_next_page(browser):
    browser.get("https://www.demoblaze.com/")
    login_page = LoginPage(browser)
    login_page.open_login_modal()
    login_page.login("user_test123123", "test123")
    time.sleep(3)
    products_page = ProductsPage(browser)
    products_page.go_to_next_page()
    time.sleep(2)
    product_name = "Apple monitor 24"
    product_element = browser.find_element(By.LINK_TEXT, product_name)
    browser.execute_script("arguments[0].scrollIntoView();", product_element)
    time.sleep(2)
    product_element.click()
    detail_title = browser.find_element(By.CLASS_NAME, "name").text
    assert detail_title == product_name, "Product name does not match on detail page"


def test_add_to_cart(browser):
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

