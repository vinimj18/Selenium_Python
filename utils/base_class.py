import pytest

from page_objects.dashboard_page import DashboardPage
from page_objects.login_page import LoginPage
from page_objects.new_employee_page import NewEmployeePage
from page_objects.pim_page import PIMPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Using BaseClass to make all tests have access to the WebDriver setup and shared methods.


@pytest.mark.usefixtures('setup')
class BaseClass:

    driver = None

    # Reusable Methods

    def login(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.enter_user().send_keys(username)
        login_page.enter_password().send_keys(password)
        login_page.get_login_button().click()

    def drop_down_selection(self, arrow_element, dropdown_locator, value):
        if arrow_element != None:
            arrow_element.click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(dropdown_locator))
        options = self.driver.find_elements(*dropdown_locator)

        for option in options:
            if option.text.strip() == value:
                option.click()
                break

    def add_new_employee(self, username, password, first_name, last_name):

        self.login(username, password)

        dashboard_page = DashboardPage(self.driver)
        dashboard_page.get_menu_pim().click()

        pim_page = PIMPage(self.driver)
        pim_page.get_add_employee_button().click()

        new_employee_page = NewEmployeePage(self.driver)
        new_employee_page.get_first_name().send_keys(first_name)
        new_employee_page.get_last_name().send_keys(last_name)
        employee_id = new_employee_page.get_employee_id().get_attribute('value')
        new_employee_page.get_save_button().click()

        return employee_id

    def search_employee(self, username, password, first_name, last_name):

        employee_id = self.add_new_employee(
            username, password, first_name, last_name)
        WebDriverWait(self.driver, 10).until(
            EC.url_changes(self.driver.current_url))

        dashboard_page = DashboardPage(self.driver)
        dashboard_page.get_menu_pim().click()

        pim_page = PIMPage(self.driver)
        pim_page.get_employee_name_field().send_keys(
            f'{first_name} {last_name}')
        pim_page.wait.until(
            EC.element_to_be_clickable((pim_page.search_button)))
        pim_page.get_search_button().click()
        pim_page.wait_results()
        pim_page.get_row_by_employee_id(employee_id)
        pim_page.wait_for_table_to_reload()
        return [pim_page.get_cells_by_employee_id(employee_id), employee_id]

    def get_cells_by_employee_id(self, employee_id):
        pim_page = PIMPage(self.driver)
        return pim_page.get_cells_by_employee_id(employee_id)
