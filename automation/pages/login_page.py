from selenium.webdriver.common.by import By

class LoginPage:

    url = "https://www.saucedemo.com/"

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def login(self, user, password):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()