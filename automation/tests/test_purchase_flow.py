import time
from automation.pages.login_page import LoginPage
from automation.pages.inventory_page import InventoryPage


def test_login_valid(driver):

    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url


def test_add_product_to_cart(driver):

        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        inventory.add_backpack()  # adiciona produto
        inventory.open_cart()  # abre carrinho
        assert "cart" in driver.current_url


def test_multiple_products(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")
    inventory.add_backpack()
    inventory.add_bike_light()

    assert "inventory" in driver.current_url


def test_login_invalid(driver):

    login = LoginPage(driver)

    login.open()
    login.login("wrong_user", "wrong_password")

    assert "inventory" not in driver.current_url
