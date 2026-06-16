from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class ContactPage(BasePage):

    CONTACT_LINK = (By.XPATH, "//a[contains(text(),'Contact')]")

    EMAIL = (By.ID, "recipient-email")
    NAME = (By.ID, "recipient-name")
    MESSAGE = (By.ID, "message-text")

    SEND_BTN = (By.XPATH, "//button[text()='Send message']")
    CLOSE_X_BTN = (By.XPATH, "//div[@id='exampleModal']//button[@class='close']")
    CLOSE_BTN = (By.XPATH, "//div[@id='exampleModal']//button[text()='Close']")
    CONTACT_MODAL = (By.ID, "exampleModal")

    def open_contact_popup(self):
        self.find_clickable(self.CONTACT_LINK).click()
        self.find_visible(self.EMAIL)

    def send_message(self, email, name, message):
        email_field = self.find_visible(self.EMAIL)
        email_field.clear()
        email_field.send_keys(email)

        name_field = self.find_visible(self.NAME)
        name_field.clear()
        name_field.send_keys(name)

        msg_field = self.find_visible(self.MESSAGE)
        msg_field.clear()
        msg_field.send_keys(message)

        self.find_clickable(self.SEND_BTN).click()

        return self.get_alert_text_and_accept(timeout=10)

    def close_via_x(self):
        self.find_clickable(self.CLOSE_X_BTN).click()
        self.is_not_visible(self.CONTACT_MODAL, timeout=5)

    def close_via_button(self):
        self.find_clickable(self.CLOSE_BTN).click()
        self.is_not_visible(self.CONTACT_MODAL, timeout=5)

    def close_with_esc(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        self.is_not_visible(self.CONTACT_MODAL, timeout=5)

    def is_modal_open(self):
        return self.is_visible(self.EMAIL, timeout=5)