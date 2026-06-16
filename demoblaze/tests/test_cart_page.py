from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class TestCart:

    def test_open_cart_page(self, driver):
        home = HomePage(driver)
        home.open()

        home.find_clickable(HomePage.CART_LINK).click()

        assert "cart" in driver.current_url


    def test_place_order_button_is_visible(self, driver):
        cart = CartPage(driver)
        cart.open()

        assert cart.is_visible(CartPage.PLACE_ORDER_BTN)


    def test_empty_cart(self, driver):
        cart = CartPage(driver)
        cart.open()

        assert len(cart.get_cart_items()) == 0


    def test_add_single_product_to_cart(self, driver):
        home = HomePage(driver)
        home.open()

        home.pause(2)
        home.click_first_product()

        product = ProductPage(driver)
        product.click_add_to_cart()

        cart = CartPage(driver)
        cart.open()

        assert len(cart.get_cart_items()) > 0


    def test_add_multiple_products_to_cart(self, driver):
        home = HomePage(driver)
        home.open()

        home.pause(2)
        home.click_first_product()

        product = ProductPage(driver)
        product.click_add_to_cart()

        home.open()
        home.pause(2)
        home.click_product_by_index(1)

        product = ProductPage(driver)
        product.click_add_to_cart()

        cart = CartPage(driver)
        cart.open()
        home.pause(5)  

        assert len(cart.get_cart_items()) >= 2


    def test_cart_total_matches_product_prices(self, driver):
        home = HomePage(driver)
        home.open()

        home.pause(2)
        home.click_first_product()

        product = ProductPage(driver)
        product.click_add_to_cart()
        
        home.open()
        home.pause(2)
        home.click_product_by_index(1)

        product = ProductPage(driver)
        product.click_add_to_cart()

        cart = CartPage(driver)
        cart.open()
        home.pause(5)

        item_prices = cart.get_item_prices()
        total_val = cart.get_total()

        if isinstance(total_val, str):
            assert total_val.isdigit(), f"Expected a numeric total text, but got: '{total_val}'"
            total = int(total_val)
        else:
            total = total_val

        assert total == sum(item_prices)


    def test_delete_product_from_cart(self, driver):
        home = HomePage(driver)
        home.open()

        home.pause(2)
        home.click_first_product()

        product = ProductPage(driver)
        product.click_add_to_cart()

        cart = CartPage(driver)
        cart.open()

        before = len(cart.get_cart_items())

        cart.delete_first_item()

        after = len(cart.get_cart_items())

        assert after < before


    def test_total_updates_after_item_deletion(self, driver):
        home = HomePage(driver)
        home.open()

        home.pause(2)
        home.click_first_product()

        product = ProductPage(driver)
        product.click_add_to_cart()
        
        home.open()
        home.pause(2)
        home.click_product_by_index(1)

        product = ProductPage(driver)
        product.click_add_to_cart()

        cart = CartPage(driver)
        cart.open()
        home.pause(5)

        before_val = cart.get_total()
        
        if isinstance(before_val, str):
            before = int(before_val) if before_val.isdigit() else 0
        else:
            before = before_val

        cart.delete_first_item()
        home.pause(4)

        after_val = cart.get_total()
        
        if isinstance(after_val, str):
            after = int(after_val) if after_val.isdigit() else 0
        else:
            after = after_val

        assert after < before


    def test_place_order_popup_opens(self, driver):
        home = HomePage(driver)
        home.open()

        home.pause(2)
        home.click_first_product()

        product = ProductPage(driver)
        product.click_add_to_cart()

        cart = CartPage(driver)
        cart.open()

        cart.open_place_order_popup()

        assert cart.is_visible(CartPage.ORDER_MODAL)


    def test_order_form_fields_are_visible(self, driver):
        home = HomePage(driver)
        home.open()

        home.pause(2)
        home.click_first_product()

        product = ProductPage(driver)
        product.click_add_to_cart()

        cart = CartPage(driver)
        cart.open()

        cart.open_place_order_popup()

        assert cart.is_visible(CartPage.ORDER_NAME)


    def test_order_popup_displays_correct_total(self, driver):
        home = HomePage(driver)
        home.open()

        home.pause(2)
        home.click_first_product()

        product = ProductPage(driver)
        product.click_add_to_cart()

        cart = CartPage(driver)
        cart.open()
        home.pause(3)

        total = int(cart.get_total())

        cart.open_place_order_popup()

        modal_total = cart.get_modal_total()

        assert str(total) in modal_total


    def test_successful_purchase(self, driver):
        home = HomePage(driver)
        home.open()

        home.pause(2)
        home.click_first_product()

        product = ProductPage(driver)
        product.click_add_to_cart()

        cart = CartPage(driver)
        cart.open()

        cart.open_place_order_popup()

        cart.fill_order_form(
            "John",
            "USA",
            "New York",
            "4532015112830366",
            "12",
            "2027"
        )

        cart.click_purchase()

        assert cart.is_order_confirmed()


    def test_purchase_with_empty_form(self, driver):
        home = HomePage(driver)
        home.open()

        home.pause(2)
        home.click_first_product()

        product = ProductPage(driver)
        product.click_add_to_cart()

        cart = CartPage(driver)
        cart.open()

        cart.open_place_order_popup()

        assert cart.click_purchase_and_get_alert() is not None


    def test_cart_page_persists_after_refresh(self, driver):
        home = HomePage(driver)
        home.open()

        home.pause(2)
        home.click_first_product()

        product = ProductPage(driver)
        product.click_add_to_cart()

        cart = CartPage(driver)
        cart.open()

        driver.refresh()

        assert "cart" in driver.current_url


    def test_place_order_button_remains_visible_after_deletion(self, driver):
        home = HomePage(driver)
        home.open()

        home.pause(2)
        home.click_first_product()

        product = ProductPage(driver)
        product.click_add_to_cart()

        cart = CartPage(driver)
        cart.open()

        cart.delete_first_item()

        assert cart.is_visible(CartPage.PLACE_ORDER_BTN)