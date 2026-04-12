from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    add_bike = (By.ID, "add-to-cart-sauce-labs-bike-light")
# add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
# elements = driver.find_elements(By.ID, "add-to-cart-sauce-labs-backpack")
    add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_product(self):
        self.driver.find_element(*self.add_backpack).click()

    def add_backpack(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def add_bike_light(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()

        wait = WebDriverWait(self.driver, 10)
        cart = wait.until(EC.element_to_be_clickable(self.cart_icon))
        cart.click()



