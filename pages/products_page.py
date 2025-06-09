# pages/products_page.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.next_product = (By.CLASS_NAME,"carousel-control-next-icon")

    def get_all_product_titles(self):
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, ".card-title")
        return [el.text for el in product_elements]

    def click_first_product(self):
        first_product = self.driver.find_element(By.CSS_SELECTOR, ".card-title")
        first_product.click()

    def get_number_of_products_displayed(self):
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, ".card.h-100")
        return len(product_elements)

    def get_product_title_on_details_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".name").text

    def click_add_to_cart(self):
        add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart"))
        )
        add_btn.click()

    def go_to_cart(self):
        self.driver.find_element(By.ID,"cartur").click()

    def go_to_next_page(self):
        self.driver.find_element(By.ID, "next2").click()