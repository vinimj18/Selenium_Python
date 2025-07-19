from utils.base_class import BaseClass
from page_objects.new_employee_page import NewEmployeePage
from page_objects.pim_page import PIMPage
from page_objects.dashboard_page import DashboardPage
from page_objects.personal_details_page import PersonalDetailsPage
from test_data.login_credentials import login_credentials
from test_data.employees import test_employee_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import time

from selenium.webdriver.common.by import By


# TEST DATA
username = login_credentials['username']
password = login_credentials['password']
first_name = test_employee_data[3]['first_name']
last_name = test_employee_data[3]['last_name']
nationality = test_employee_data[3]['nationality']
year = test_employee_data[3]['year']
month = test_employee_data[3]['month']
day = test_employee_data[3]['day']


@pytest.mark.usefixtures('setup')
class TestUpdateEmployee(BaseClass):

    def test_update_employee(self, setup):
        driver = setup
        new_employee_page = NewEmployeePage(driver)

        employee_id = new_employee_page.add_new_employee(
            username, password, first_name, last_name)
        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))

        dashboard_page = DashboardPage(driver)
        dashboard_page.get_menu_pim().click()

        pim_page = PIMPage(driver)

        pim_page.search_employee(first_name, last_name, employee_id)

        pim_page.wait_for_id_tobe_clickable(employee_id)
        cells = pim_page.get_cells_by_employee_id(employee_id)
        cells[1].click()

        personal_details_page = PersonalDetailsPage(driver)

        arrow = personal_details_page.open_nationality_dd()

        self.drop_down_selection(arrow,
                                 personal_details_page.nationality_dropdown,
                                 nationality)

        personal_details_page.open_dob_calendar().click()
        time.sleep(5)

        # self.drop_down_selection(personal_details_page.get_month(),
        #                          personal_details_page.calendar_dropdown,
        #                          month)
        # self.drop_down_selection(personal_details_page.get_year(),
        #                          personal_details_page.calendar_dropdown,
        #                          year)

        personal_details_page.select_calendar_month(month)
        personal_details_page.select_calendar_year(year)
        personal_details_page.get_day(day)

        personal_details_page.get_day(day).click()

        time.sleep(3)
        driver.find_element(By.TAG_NAME, 'body').click()
        personal_details_page.get_save_button().click()

        time.sleep(3)
        assert personal_details_page.get_nationality() == nationality
        assert day in personal_details_page.get_dob()
        assert month in personal_details_page.get_dob()
        assert year in personal_details_page.get_dob()
