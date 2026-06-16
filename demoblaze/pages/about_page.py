from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class AboutPage(BasePage):

    ABOUT_LINK = (By.XPATH, "//a[contains(text(),'About us')]")
    ABOUT_MODAL = (By.ID, "videoModal")
    VIDEO_PLAYER = (By.CSS_SELECTOR, "#videoModal video")

    CLOSE_BTN = (By.XPATH, "//div[@id='videoModal']//button[text()='Close']")
    CLOSE_X_BTN = (By.XPATH, "//div[@id='videoModal']//button[@class='close']")

    
    def open_about_popup(self):
        self.find_clickable(self.ABOUT_LINK).click()
        self.find_visible(self.ABOUT_MODAL)

    
    def is_video_present(self):
        return self.is_visible(self.VIDEO_PLAYER, timeout=5)

    def play_video(self):
        video = self.find_visible(self.VIDEO_PLAYER)
        self.driver.execute_script("arguments[0].play();", video)

    def pause_video(self):
        video = self.find_visible(self.VIDEO_PLAYER)
        self.driver.execute_script("arguments[0].pause();", video)

    def is_video_playing(self):
        video = self.find_visible(self.VIDEO_PLAYER)
        return self.driver.execute_script("return !arguments[0].paused;", video)

    
    def close_via_x(self):
        self.find_clickable(self.CLOSE_X_BTN).click()
        self.is_not_visible(self.ABOUT_MODAL, timeout=5)

    def close_via_button(self):
        self.find_clickable(self.CLOSE_BTN).click()
        self.is_not_visible(self.ABOUT_MODAL, timeout=5)

    def close_with_esc(self):
        
        self.find_visible(self.ABOUT_MODAL).click()
        self.driver.switch_to.active_element.send_keys(Keys.ESCAPE)
        self.is_not_visible(self.ABOUT_MODAL, timeout=5)

    def click_outside_popup(self):
        self.driver.execute_script(
            "document.elementFromPoint(5, 5).click();"
        )
        self.pause(1)