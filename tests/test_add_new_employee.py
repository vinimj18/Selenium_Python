from page_objects.new_employee_page import NewEmployeePage
from test_data.test_data import data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from utils.base_class import BaseClass

# TEST DATA
login_data = data['login']
employee_data = data['add_new_employee']


class TestNewEmployee(BaseClass):

    def test_add_new_employee(self):

        # Test Navigation
        new_employee_page = NewEmployeePage(self.driver)

        self.add_new_employee(
            login_data['username'],
            login_data['password'],
            employee_data['first_name'],
            employee_data['last_name'])

        # Test Assertions
        assert "Success" in new_employee_page.get_pop_up().text
        WebDriverWait(self.driver, 10).until(
            EC.url_changes(self.driver.current_url))
        assert "PersonalDetails" in self.driver.current_url
