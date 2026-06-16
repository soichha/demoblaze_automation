from pages.contact_page import ContactPage


class TestContact:

    def test_contact_popup_opens(self, driver):
        page = ContactPage(driver)
        page.open()
        page.open_contact_popup()

        assert page.is_visible(ContactPage.CONTACT_MODAL)

    def test_contact_form_fields_are_visible(self, driver):
        page = ContactPage(driver)
        page.open()
        page.open_contact_popup()

        assert page.is_visible(ContactPage.NAME)
        assert page.is_visible(ContactPage.EMAIL)
        assert page.is_visible(ContactPage.MESSAGE)
        assert page.is_visible(ContactPage.SEND_BTN)

    def test_send_message_with_valid_data(self, driver):
        page = ContactPage(driver)
        page.open()
        page.open_contact_popup()
        alert = page.send_message("test@test.com", "John", "Hello")

        assert alert is not None

    def test_send_message_with_empty_fields(self, driver):
        page = ContactPage(driver)
        page.open()
        page.open_contact_popup()

        alert = page.send_message("", "John", "Hello")

        assert alert is not None

    def test_send_message_with_invalid_email(self, driver):
        page = ContactPage(driver)
        page.open()
        page.open_contact_popup()

        alert = page.send_message("invalid", "John", "Hello")

        assert alert is not None

    def test_send_message_with_long_message(self, driver):
        page = ContactPage(driver)
        page.open()
        page.open_contact_popup()

        
        alert = page.send_message("test@test.com", "John", "A" * 100)

        assert alert is not None

    def test_close_contact_popup_with_x(self, driver):
        page = ContactPage(driver)
        page.open()
        page.open_contact_popup()

        page.close_via_x()

        page.pause(1)
        assert page.is_not_visible(ContactPage.CONTACT_MODAL, timeout=5)

    def test_close_contact_popup_with_escape(self, driver):
        page = ContactPage(driver)
        page.open()
        page.open_contact_popup()

        page.close_with_esc()

        page.pause(1)
        assert page.is_not_visible(ContactPage.CONTACT_MODAL, timeout=5)

    def test_contact_popup_reopens(self, driver):
        page = ContactPage(driver)
        page.open()
        page.open_contact_popup()

        page.send_message("test@test.com", "John", "Hello")

        page.open_contact_popup()

        assert page.is_visible(ContactPage.CONTACT_MODAL)

    def test_contact_link_exists(self, driver):
        page = ContactPage(driver)
        page.open()

        assert page.is_visible(ContactPage.CONTACT_LINK)


    def test_invalid_email_should_be_rejected(self, driver):
        page = ContactPage(driver)
        page.open()
        page.open_contact_popup()

        alert = page.send_message("notanemail", "John", "Hello test")

        assert alert is not None
        assert "thanks" not in alert.lower(), (
            "BUG: contact form should reject invalid email format"
        )