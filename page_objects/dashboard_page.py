from selenium.webdriver.common.by import By


class DashboardPage:

    def __init__(self, driver) -> None:
        self.driver = driver

    # Locators
    header = (By.CLASS_NAME, 'oxd-topbar-header-title')
    menu = (By.CLASS_NAME, 'oxd-main-menu')
    card = (By.CLASS_NAME, 'orangehrm-dashboard-widget')
    menu_pim = (By.CLASS_NAME, 'oxd-main-menu-item')
    user_dropdown_arrow = (By.CLASS_NAME, 'oxd-userdropdown-icon')
    logout_link = (By.CLASS_NAME, 'oxd-userdropdown-link')

    # Elements
    def get_header(self):
        return self.driver.find_element(*DashboardPage.header)

    def get_menu(self):
        return self.driver.find_element(*DashboardPage.menu)

    def get_card(self):
        return self.driver.find_element(*DashboardPage.card)

    def get_menu_pim(self):
        return self.driver.find_elements(*DashboardPage.menu_pim)[1]

    def get_dropdown_arrow(self):
        return self.driver.find_element(*DashboardPage.user_dropdown_arrow)

    def get_logout_link(self):
        return self.driver.find_elements(*DashboardPage.logout_link)[3]
