from page_objects.new_employee_page import NewEmployeePage
from page_objects.pim_page import PIMPage
from test_data.login_credentials import login_credentials
from test_data.employees import test_employee_data
import time
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

        pim_page = PIMPage(driver)
        assert "Success" in new_employee_page.get_pop_up().text
        pim_page.get_current_url()
        assert "PersonalDetails" in driver.current_url
