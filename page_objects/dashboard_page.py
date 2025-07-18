from selenium.webdriver.common.by import By
import pytest


class DashboardPage:

    def __init__(self, driver) -> None:
        self.driver = driver

    header = (By.CLASS_NAME, 'oxd-topbar-header-title')
    menu = (By.CLASS_NAME, 'oxd-main-menu')
    card = (By.CLASS_NAME, 'orangehrm-dashboard-widget')
    menu_pim = (By.CLASS_NAME, 'oxd-main-menu-item')

    def get_header(self):
        return self.driver.find_element(*DashboardPage.header)

    def get_menu(self):
        return self.driver.find_element(*DashboardPage.menu)

    def get_card(self):
        return self.driver.find_element(*DashboardPage.card)

    def get_menu_pim(self):
        return self.driver.find_elements(*DashboardPage.menu_pim)[1]
