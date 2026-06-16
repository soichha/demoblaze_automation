from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    LOGIN_LINK = (By.ID, "login2")
    SIGNUP_LINK = (By.ID, "signin2")
    LOGOUT_LINK = (By.ID, "logout2")
    CART_LINK = (By.ID, "cartur")
    USERNAME_LABEL = (By.ID, "nameofuser")

    LOGIN_USERNAME = (By.ID, "loginusername")
    LOGIN_PASSWORD = (By.ID, "loginpassword")
    LOGIN_BTN = (By.XPATH, "//button[text()='Log in']")

    SIGNUP_USERNAME = (By.ID, "sign-username")
    SIGNUP_PASSWORD = (By.ID, "sign-password")
    SIGNUP_BTN = (By.XPATH, "//button[text()='Sign up']")

    PRODUCT_LINKS = (By.CSS_SELECTOR, ".card-title a")
    PHONES_BTN = (By.XPATH, "//a[text()='Phones']")
    LAPTOPS_BTN = (By.XPATH, "//a[text()='Laptops']")
    MONITORS_BTN = (By.XPATH, "//a[text()='Monitors']")

    NEXT_BTN = (By.CSS_SELECTOR, ".carousel-control-next")
    PREV_BTN = (By.CSS_SELECTOR, ".carousel-control-prev")
    BANNER = (By.CSS_SELECTOR, ".carousel-inner")

    LOGIN_MODAL = (By.ID, "logInModal")
    LOGIN_CLOSE_X = (By.XPATH, "//div[@id='logInModal']//button[@class='close']")
    LOGIN_CLOSE_BTN = (By.XPATH, "//div[@id='logInModal']//button[text()='Close']")

    SIGNUP_MODAL = (By.ID, "signInModal")
    SIGNUP_CLOSE_X = (By.XPATH, "//div[@id='signInModal']//button[@class='close']")
    SIGNUP_CLOSE_BTN = (By.XPATH, "//div[@id='signInModal']//button[text()='Close']")

    def open_login_popup(self):
        self.find_clickable(self.LOGIN_LINK).click()
        self.find_visible(self.LOGIN_MODAL)
        self.find_visible(self.LOGIN_USERNAME)

    def do_login(self, username, password):
        self.find_element(self.LOGIN_USERNAME).clear()
        self.find_element(self.LOGIN_USERNAME).send_keys(username)

        self.find_element(self.LOGIN_PASSWORD).clear()
        self.find_element(self.LOGIN_PASSWORD).send_keys(password)

        self.find_clickable(self.LOGIN_BTN).click()

    def open_signup_popup(self):
        self.find_clickable(self.SIGNUP_LINK).click()
        self.find_visible(self.SIGNUP_MODAL)
        self.find_visible(self.SIGNUP_USERNAME)

    def do_signup(self, username, password):
        self.find_element(self.SIGNUP_USERNAME).clear()
        self.find_element(self.SIGNUP_USERNAME).send_keys(username)

        self.find_element(self.SIGNUP_PASSWORD).clear()
        self.find_element(self.SIGNUP_PASSWORD).send_keys(password)

        self.find_clickable(self.SIGNUP_BTN).click()

    def _get_products(self):
        return self.wait.until(
            lambda d: d.find_elements(*self.PRODUCT_LINKS)
        )

    def click_first_product(self):
        products = self._get_products()
        products[0].click()

    def click_product_by_index(self, index):
        products = self._get_products()
        products[index].click()

    def get_all_product_names(self):
        products = self._get_products()
        return [p.text for p in products]

    def get_first_product_info(self):
        card = self.driver.find_element(By.CSS_SELECTOR, ".card")
        name = card.find_element(By.CSS_SELECTOR, ".card-title").text
        price = card.find_element(By.CSS_SELECTOR, "h5").text
        return name, price

    def click_category(self, name):
        categories = {
            "phones": self.PHONES_BTN,
            "laptops": self.LAPTOPS_BTN,
            "monitors": self.MONITORS_BTN,
        }
        self.find_clickable(categories[name.lower()]).click()

    def is_logged_in(self):
        return self.is_visible(self.USERNAME_LABEL)

    def do_logout(self):
        self.find_clickable(self.LOGOUT_LINK).click()

    def get_signup_username_value(self):
        return self.find_element(self.SIGNUP_USERNAME).get_attribute("value")

    def get_signup_password_value(self):
        return self.find_element(self.SIGNUP_PASSWORD).get_attribute("value")

    def get_login_username_value(self):
        return self.find_element(self.LOGIN_USERNAME).get_attribute("value")

    def get_login_password_value(self):
        return self.find_element(self.LOGIN_PASSWORD).get_attribute("value")