from pages.home_page import HomePage


class TestHomePage:

    def test_home_page_loads_successfully(self, driver):
        page = HomePage(driver)
        page.open()

        assert "demoblaze.com" in driver.current_url

    def test_login_link_is_visible(self, driver):
        page = HomePage(driver)
        page.open()

        assert page.is_visible(HomePage.LOGIN_LINK)

    def test_navigation_arrows_work(self, driver):
        page = HomePage(driver)
        page.open()

        page.find_clickable(HomePage.NEXT_BTN).click()
        page.find_clickable(HomePage.PREV_BTN).click()

        assert page.is_visible(HomePage.PREV_BTN)

    def test_category_phones_has_products(self, driver):
        page = HomePage(driver)
        page.open()

        page.click_category("phones")

        assert len(page.get_all_product_names()) > 0

    def test_category_laptops_has_products(self, driver):
        page = HomePage(driver)
        page.open()

        page.click_category("laptops")

        assert len(page.get_all_product_names()) > 0

    def test_category_monitors_has_products(self, driver):
        page = HomePage(driver)
        page.open()

        page.click_category("monitors")

        assert len(page.get_all_product_names()) > 0

    def test_click_first_product_opens_details_page(self, driver):
        page = HomePage(driver)
        page.open()

        page.click_first_product()

        assert "prod.html" in driver.current_url

    def test_cart_page_navigation(self, driver):
        page = HomePage(driver)
        page.open()

        page.find_clickable(HomePage.CART_LINK).click()

        assert "cart" in driver.current_url

    def test_responsive_layout_mobile_view(self, driver):
        driver.set_window_size(375, 667)

        page = HomePage(driver)
        page.open()

        assert page.is_visible(HomePage.LOGIN_LINK)

        driver.maximize_window()

    def test_footer_is_visible_on_scroll(self, driver):
        page = HomePage(driver)
        page.open()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        footer = driver.find_element("tag name", "footer")

        assert footer.is_displayed()

    def test_bug_01_banner_visible_on_mobile(self, driver):
        driver.set_window_size(375, 667)

        page = HomePage(driver)
        page.open()

        assert page.is_visible(HomePage.BANNER, timeout=5), (
            "BUG: homepage banner/carousel should be visible on mobile"
        )

        driver.maximize_window()