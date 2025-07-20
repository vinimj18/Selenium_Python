from page_objects.new_employee_page import NewEmployeePage
from utils.base_class import BaseClass
from page_objects.pim_page import PIMPage
from page_objects.dashboard_page import DashboardPage
from test_data.test_data import data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest

# TEST DATA
login_data = data['login']
employee_data = data['search_employee']


@pytest.mark.usefixtures('setup')
class TestSearchEmployee(BaseClass):

    def test_search_employee(self):

        cells, employee_id = self.search_employee(
            login_data['username'],
            login_data['password'],
            employee_data['first_name'],
            employee_data['last_name']
        )

        assert cells[2].text == employee_data['first_name']
        assert cells[3].text == employee_data['last_name']
        assert cells[1].text == employee_id
