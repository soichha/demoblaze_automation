from pages.home_page import HomePage


class TestSignup:

    def test_signup_fields_are_visible(self, driver):
        page = HomePage(driver)
        page.open()
        page.open_signup_popup()

        assert page.is_visible(HomePage.SIGNUP_USERNAME)
        assert page.is_visible(HomePage.SIGNUP_PASSWORD)

    def test_signup_password_is_masked(self, driver):
        page = HomePage(driver)
        page.open()
        page.open_signup_popup()

        field = page.find_element(HomePage.SIGNUP_PASSWORD)
        assert field.get_attribute("type") == "password"

    def test_successful_signup(self, driver):
        page = HomePage(driver)
        page.open()
        page.open_signup_popup()

        user = f"user_{int(__import__('time').time())}"
        page.do_signup(user, "test123")

        alert = page.get_alert_text_and_accept()
        assert alert is not None

    def test_existing_user_signup(self, driver):
        page = HomePage(driver)
        page.open()
        page.open_signup_popup()

        page.do_signup("testsme", "test123")

        alert = page.get_alert_text_and_accept()
        assert alert is not None
        assert "exist" in alert.lower()

    def test_close_signup_modal(self, driver):
        page = HomePage(driver)
        page.open()
        page.open_signup_popup()

        page.find_clickable(HomePage.SIGNUP_CLOSE_BTN).click()

        assert page.is_not_visible(HomePage.SIGNUP_MODAL, timeout=5)