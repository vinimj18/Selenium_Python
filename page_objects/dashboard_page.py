from selenium.webdriver.common.by import By
import pytest


class DashboardPage:

    def __init__(self, driver) -> None:
        self.driver = driver

    header = (By.CLASS_NAME, 'oxd-topbar-header-title')
    menu = (By.CLASS_NAME, 'oxd-main-menu')
    card = (By.CLASS_NAME, 'orangehrm-dashboard-widget')

    def get_header(self):
        return self.driver.find_element(*DashboardPage.header)

    def get_menu(self):
        return self.driver.find_element(*DashboardPage.menu)

    def get_card(self):
        return self.driver.find_element(*DashboardPage.card)
