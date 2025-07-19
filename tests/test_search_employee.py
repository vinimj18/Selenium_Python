from page_objects.new_employee_page import NewEmployeePage
from page_objects.pim_page import PIMPage
from page_objects.dashboard_page import DashboardPage
from test_data.login_credentials import login_credentials
from test_data.employees import test_employee_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest

# TEST DATA
username = login_credentials['username']
password = login_credentials['password']
first_name = test_employee_data[1]['first_name']
last_name = test_employee_data[1]['last_name']


@pytest.mark.usefixtures('setup')
class TestSearchEmployee:

    def test_search_employee(self, setup):
        driver = setup
        new_employee_page = NewEmployeePage(driver)

        employee_id = new_employee_page.add_new_employee(
            username, password, first_name, last_name)
        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))

        dashboard_page = DashboardPage(driver)
        dashboard_page.get_menu_pim().click()

        pim_page = PIMPage(driver)

        pim_page.search_employee(first_name, last_name, employee_id)
        cells = pim_page.get_cells_by_employee_id(employee_id)

        assert cells[2].text == first_name
        assert cells[3].text == last_name
        assert cells[1].text == employee_id
