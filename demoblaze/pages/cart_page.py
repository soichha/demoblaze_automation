from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ROWS = (By.XPATH, "//tbody[@id='tbodyid']/tr")
    TOTAL_PRICE = (By.ID, "totalp")
    PLACE_ORDER_BTN = (By.XPATH, "//button[text()='Place Order']")
    DELETE_BTN = (By.XPATH, "//a[text()='Delete']")

    
    ORDER_MODAL = (By.ID, "orderModal")
    ORDER_NAME = (By.ID, "name")
    ORDER_COUNTRY = (By.ID, "country")
    ORDER_CITY = (By.ID, "city")
    ORDER_CARD = (By.ID, "card")
    ORDER_MONTH = (By.ID, "month")
    ORDER_YEAR = (By.ID, "year")

    PURCHASE_BTN = (By.XPATH, "//button[text()='Purchase']")
    MODAL_TOTAL = (By.ID, "totalm")

   
    CONFIRM_POPUP = (By.CSS_SELECTOR, ".sweet-alert")
    CONFIRM_OK_BTN = (By.CSS_SELECTOR, ".sweet-alert .confirm")

    
    def open(self):
        self.driver.get(self.BASE_URL + "cart.html")

    def get_cart_items(self):
        try:
            rows = self.wait.until(
                lambda d: d.find_elements(*self.CART_ROWS)
            )
            return [r for r in rows if r.is_displayed()]
        except:
            return []

    def is_cart_empty(self):
        return len(self.get_cart_items()) == 0

    def get_item_prices(self):
        prices = []
        for row in self.get_cart_items():
            try:
                price_text = row.find_element(By.XPATH, "./td[3]").text.strip()
                prices.append(int(price_text))
            except:
                continue
        return prices

    def get_total(self):
        try:
            self.find_element(self.TOTAL_PRICE)
            total_text = self.find_element(self.TOTAL_PRICE).text.strip()
            return int(total_text) if total_text else 0
        except:
            return 0

    def get_modal_total(self):
        try:
            self.find_element(self.MODAL_TOTAL)
            return self.find_element(self.MODAL_TOTAL).text.strip()
        except:
            return ""

    def clear_cart(self):
        while True:
            buttons = self.driver.find_elements(*self.DELETE_BTN)
            if not buttons:
                break

            btn = buttons[0]
            btn.click()

            try:
                self.wait.until(EC.staleness_of(btn))
            except TimeoutException:
                break

    def delete_first_item(self):
        buttons = self.driver.find_elements(*self.DELETE_BTN)
        if buttons:
            btn = buttons[0]
            btn.click()
            try:
                self.wait.until(EC.staleness_of(btn))
            except TimeoutException:
                pass


    def open_place_order_popup(self):
        self.find_clickable(self.PLACE_ORDER_BTN).click()
        self.find_visible(self.ORDER_NAME)

    def fill_order_form(self, name, country, city, card, month, year):
        self.find_element(self.ORDER_NAME).clear()
        self.find_element(self.ORDER_NAME).send_keys(name)

        self.find_element(self.ORDER_COUNTRY).clear()
        self.find_element(self.ORDER_COUNTRY).send_keys(country)

        self.find_element(self.ORDER_CITY).clear()
        self.find_element(self.ORDER_CITY).send_keys(city)

        self.find_element(self.ORDER_CARD).clear()
        self.find_element(self.ORDER_CARD).send_keys(card)

        self.find_element(self.ORDER_MONTH).clear()
        self.find_element(self.ORDER_MONTH).send_keys(month)

        self.find_element(self.ORDER_YEAR).clear()
        self.find_element(self.ORDER_YEAR).send_keys(year)

    def click_purchase(self):
        self.find_clickable(self.PURCHASE_BTN).click()

    def click_purchase_and_get_alert(self):
        self.click_purchase()
        return self.get_alert_text_and_accept(timeout=10)

    
    def is_order_confirmed(self):
        return self.is_visible(self.CONFIRM_POPUP, timeout=10)

    def close_confirmation(self):
        self.find_clickable(self.CONFIRM_OK_BTN).click()
        self.is_not_visible(self.CONFIRM_POPUP, timeout=10)