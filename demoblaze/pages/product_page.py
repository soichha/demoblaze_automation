from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):

    PRODUCT_NAME    = (By.CSS_SELECTOR, ".name")
    PRODUCT_PRICE   = (By.CSS_SELECTOR, ".price-container")
    PRODUCT_DESC    = (By.CSS_SELECTOR, ".description")
    PRODUCT_IMAGE   = (By.CSS_SELECTOR, ".item.active img")
    ADD_TO_CART_BTN = (By.XPATH, "//a[text()='Add to cart']")

    def get_product_name(self):
        return self.find_element(self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.find_element(self.PRODUCT_PRICE).text

    def is_image_displayed(self):
        return self.find_element(self.PRODUCT_IMAGE).is_displayed()

    def click_add_to_cart(self):
        self.find_clickable(self.ADD_TO_CART_BTN).click()

        return self.get_alert_text_and_accept(timeout=10)

    def add_to_cart(self):
        return self.click_add_to_cart()

    
    def go_back(self):
        self.driver.back()
        self.pause(1)

    def open_invalid_product(self, product_id=99999):
        self.driver.get(self.BASE_URL + f"prod.html?id={product_id}")
        self.pause(2)