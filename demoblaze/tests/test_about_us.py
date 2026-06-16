from pages.about_page import AboutPage


class TestAbout:

    def test_about_popup_opens(self, driver):
        page = AboutPage(driver)
        page.open()
        page.open_about_popup()

        assert page.is_visible(AboutPage.ABOUT_MODAL)

    def test_video_player_is_visible(self, driver):
        page = AboutPage(driver)
        page.open()
        page.open_about_popup()

        assert page.is_visible(AboutPage.VIDEO_PLAYER)

    def test_video_can_play(self, driver):
        page = AboutPage(driver)
        page.open()
        page.open_about_popup()

        page.play_video()

        assert page.is_video_playing()

    def test_video_can_pause(self, driver):
        page = AboutPage(driver)
        page.open()
        page.open_about_popup()

        page.play_video()
        page.pause_video()

        page.pause(2)
        assert not page.is_video_playing()

    def test_close_popup_using_x(self, driver):
        page = AboutPage(driver)
        page.open()
        page.open_about_popup()

        page.close_via_x()

        page.pause(2)
        assert page.is_not_visible(AboutPage.ABOUT_MODAL, timeout=5)

    def test_close_popup_using_close_button(self, driver):
        page = AboutPage(driver)
        page.open()
        page.open_about_popup()

        page.close_via_button()

        page.pause(2)
        assert page.is_not_visible(AboutPage.ABOUT_MODAL, timeout=5)

    def test_close_popup_using_escape_key(self, driver):
        page = AboutPage(driver)
        page.open()
        page.open_about_popup()

        page.close_with_esc()

        page.pause(2)
        assert page.is_not_visible(AboutPage.ABOUT_MODAL, timeout=5)

    def test_popup_can_be_reopened(self, driver):
        page = AboutPage(driver)
        page.open()
        page.open_about_popup()

        page.close_via_button()
        page.open_about_popup()

        page.pause(2)
        
        assert page.is_visible(AboutPage.ABOUT_MODAL, timeout=5)

    def test_about_popup_on_mobile_view(self, driver):
        driver.set_window_size(375, 667)

        page = AboutPage(driver)
        page.open()
        page.open_about_popup()

        page.pause(2)
      
        assert page.is_visible(AboutPage.ABOUT_MODAL, timeout=5)

        driver.maximize_window()