from pages.home_page import HomePage


class TestLogin:

    def test_login_modal_opens(self, driver):
        page = HomePage(driver)
        page.open()
        page.open_login_popup()

        assert page.is_visible(HomePage.LOGIN_MODAL)

    def test_login_fields_are_visible(self, driver):
        page = HomePage(driver)
        page.open()
        page.open_login_popup()

        assert page.is_visible(HomePage.LOGIN_USERNAME)
        assert page.is_visible(HomePage.LOGIN_PASSWORD)

    def test_password_field_type_is_password(self, driver):
        page = HomePage(driver)
        page.open()
        page.open_login_popup()

        field = page.find_element(HomePage.LOGIN_PASSWORD)

        assert field.get_attribute("type") == "password"

    def test_successful_login(self, driver):
        page = HomePage(driver)
        page.open()
        page.open_login_popup()

        page.do_login("testsme", "test123")

        assert page.is_logged_in()

    def test_login_invalid_credentials_shows_alert(self, driver):
        page = HomePage(driver)
        page.open()
        page.open_login_popup()

        page.do_login("testsme", "wrongpassword")

        alert = page.get_alert_text_and_accept()

        assert alert is not None
        assert "wrong" in alert.lower()

    def test_login_empty_credentials_shows_alert(self, driver):
        page = HomePage(driver)
        page.open()
        page.open_login_popup()

        page.do_login("", "")

        alert = page.get_alert_text_and_accept()

        assert alert is not None

    def test_close_login_modal_with_button(self, driver):
        page = HomePage(driver)
        page.open()
        page.open_login_popup()

        page.find_clickable(HomePage.LOGIN_CLOSE_BTN).click()

        assert page.is_not_visible(HomePage.LOGIN_MODAL)

    def test_close_login_modal_with_x(self, driver):
        page = HomePage(driver)
        page.open()
        page.open_login_popup()

        page.find_clickable(HomePage.LOGIN_CLOSE_X).click()

        assert page.is_not_visible(HomePage.LOGIN_MODAL)

    def test_logout_after_successful_login(self, driver):
        page = HomePage(driver)
        page.open()
        page.open_login_popup()

        page.do_login("testsme", "test123")
        page.do_logout()

        assert page.is_visible(HomePage.LOGIN_LINK)

    def test_username_display_after_login(self, driver):
        page = HomePage(driver)
        page.open()
        page.open_login_popup()

        page.do_login("testsme", "test123")

        username = page.find_visible(HomePage.USERNAME_LABEL).text.lower()

        assert "testsme" in username

    
    def test_login_fields_cleared_after_reopen(self, driver):
        page = HomePage(driver)
        page.open()
        page.open_login_popup()

        page.find_element(HomePage.LOGIN_USERNAME).send_keys("testsme")
        page.find_element(HomePage.LOGIN_PASSWORD).send_keys("test123")
        page.find_clickable(HomePage.LOGIN_CLOSE_X).click()
        page.pause(1)

        page.open_login_popup()

        assert page.get_login_username_value() == "", (
            "BUG: login username should be empty after reopen"
        )
        assert page.get_login_password_value() == "", (
            "BUG: login password should be empty after reopen"
        )