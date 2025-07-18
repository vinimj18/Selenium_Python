from page_objects.new_employee_page import NewEmployeePage
from test_data.login_credentials import login_credentials
from test_data.employees import test_employee_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# TEST DATA
username = login_credentials['username']
password = login_credentials['password']
first_name = test_employee_data[0]['first_name']
last_name = test_employee_data[0]['last_name']


@pytest.mark.usefixtures('setup')
class TestNewEmployee:

    def test_add_new_employee(self, setup):
        driver = setup
        new_employee_page = NewEmployeePage(driver)

        new_employee_page.add_new_employee(
            username, password, first_name, last_name)

        assert "Success" in new_employee_page.get_pop_up().text
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_changes(driver.current_url))
        assert "PersonalDetails" in driver.current_url
