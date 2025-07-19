from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.login_page import LoginPage
from page_objects.dashboard_page import DashboardPage
from page_objects.pim_page import PIMPage


class NewEmployeePage:

    def __init__(self, driver) -> None:
        self.driver = driver

    first_name = (By.NAME, 'firstName')
    last_name = (By.NAME, 'lastName')
    employee_id = (
        By.CSS_SELECTOR, "div[class='oxd-input-group oxd-input-field-bottom-space'] div input[class='oxd-input oxd-input--active']")
    save_button = (By.CSS_SELECTOR, "button[type='submit']")
    pop_up = (By.CSS_SELECTOR,
              'p.oxd-text.oxd-text--p.oxd-text--toast-message.oxd-toast-content-text')

    def get_first_name(self):
        return self.driver.find_element(*NewEmployeePage.first_name)

    def get_last_name(self):
        return self.driver.find_element(*NewEmployeePage.last_name)

    def get_employee_id(self):
        return self.driver.find_element(*NewEmployeePage.employee_id)

    def get_save_button(self):
        return self.driver.find_element(*NewEmployeePage.save_button)

    def get_pop_up(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(NewEmployeePage.pop_up))

    def add_new_employee(self, username, password, first_name, last_name):

        login_page = LoginPage(self.driver)
        login_page.login(username, password)

        dashboard_page = DashboardPage(self.driver)
        dashboard_page.get_menu_pim().click()

        pim_page = PIMPage(self.driver)
        pim_page.get_add_employee_button().click()

        self.get_first_name().send_keys(first_name)
        self.get_last_name().send_keys(last_name)
        employee_id = self.get_employee_id().get_attribute('value')
        self.get_save_button().click()

        return employee_id
