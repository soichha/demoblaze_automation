from pages.home_page import HomePage
from pages.product_page import ProductPage


class TestProduct:

    def test_product_page_opens(self, driver):
        home = HomePage(driver)
        home.open()
        home.click_first_product()

        assert "prod.html" in driver.current_url

    def test_product_image_is_displayed(self, driver):
        home = HomePage(driver)
        home.open()
        home.click_first_product()

        product = ProductPage(driver)

        assert product.is_image_displayed()

    def test_product_name_is_not_empty(self, driver):
        home = HomePage(driver)
        home.open()
        home.click_first_product()

        product = ProductPage(driver)

        assert product.get_product_name().strip() != ""

    def test_product_price_contains_currency_symbol(self, driver):
        home = HomePage(driver)
        home.open()
        home.click_first_product()

        product = ProductPage(driver)

        assert "$" in product.get_product_price()

    def test_add_to_cart_button_is_visible(self, driver):
        home = HomePage(driver)
        home.open()
        home.click_first_product()

        product = ProductPage(driver)

        assert product.is_visible(ProductPage.ADD_TO_CART_BTN)

    def test_add_to_cart_triggers_alert(self, driver):
        home = HomePage(driver)
        home.open()
        home.click_first_product()

        product = ProductPage(driver)

        alert = product.click_add_to_cart()

        assert alert is not None

    def test_product_name_matches_homepage(self, driver):
        home = HomePage(driver)
        home.open()

        name, _ = home.get_first_product_info()
        home.click_first_product()

        product = ProductPage(driver)

        assert name in product.get_product_name()

    def test_add_to_cart_multiple_times(self, driver):
        home = HomePage(driver)
        home.open()
        home.click_first_product()

        product = ProductPage(driver)

        product.click_add_to_cart()
        product.click_add_to_cart()

        
        alert = product.click_add_to_cart()

        assert alert is not None

    
    def test_invalid_product_url_no_undefined(self, driver):
        product = ProductPage(driver)
        product.open_invalid_product(99999)

        page_text = driver.find_element("tag name", "body").text.lower()

        assert "undefined" not in page_text, (
            "BUG: invalid product page should not display undefined values"
        )