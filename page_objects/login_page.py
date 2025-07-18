from selenium.webdriver.common.by import By
import pytest
from test_data.login_credentials import login_credentials


class LoginPage:

    def __init__(self, driver) -> None:
        self.driver = driver

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_button = (By.CLASS_NAME, 'orangehrm-login-button')

    def enter_user(self):
        return self.driver.find_element(*LoginPage.username)

    def enter_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)

    def login(self, credentials):
        self.enter_user().send_keys(credentials['username'])
        self.enter_password().send_keys(credentials['password'])
        self.get_login_button().click()
