from page_objects.new_employee_page import NewEmployeePage
from test_data.test_data import data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from utils.base_class import BaseClass

# TEST DATA
login_data = data['login']
employee_data = data['add_new_employee']


@pytest.mark.usefixtures('setup')
class TestNewEmployee(BaseClass):

    def test_add_new_employee(self, setup):
        driver = setup
        new_employee_page = NewEmployeePage(driver)

        self.add_new_employee(
            login_data['username'],
            login_data['password'],
            employee_data['first_name'],
            employee_data['last_name'])

        assert "Success" in new_employee_page.get_pop_up().text
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_changes(driver.current_url))
        assert "PersonalDetails" in driver.current_url
