from utils.base_class import BaseClass
from page_objects.personal_details_page import PersonalDetailsPage
from test_data.test_data import data

import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# TEST DATA
login_data = data['login']
employee_data = data['update_employee']


@pytest.mark.usefixtures('setup')
class TestUpdateEmployee(BaseClass):

    def test_update_employee(self, setup):
        driver = setup

        cells, employee_id = self.search_employee(
            login_data['username'],
            login_data['password'],
            employee_data['first_name'],
            employee_data['last_name']
        )
        cells[1].click()

        personal_details_page = PersonalDetailsPage(driver)

        arrow = personal_details_page.open_nationality_dd()

        self.drop_down_selection(arrow,
                                 personal_details_page.nationality_dropdown,
                                 employee_data['nationality'])

        personal_details_page.open_dob_calendar().click()

        self.drop_down_selection(personal_details_page.get_month(),
                                 personal_details_page.month_options,
                                 employee_data['mob'])
        self.drop_down_selection(personal_details_page.get_year(),
                                 personal_details_page.year_options,
                                 employee_data['yob'])
        self.drop_down_selection(None,
                                 personal_details_page.day_options,
                                 employee_data['dob'])

        # WebDriverWait(driver, 10).until_not(
        #     lambda d: d.find_element(By.CSS_SELECTOR, "ul").is_displayed()
        # )

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            personal_details_page.get_save_button())

        # time.sleep(3)
        assert personal_details_page.get_nationality(
        ) == employee_data['nationality']
        assert employee_data['dob'] in personal_details_page.get_dob()
        assert employee_data['mob_num'] in personal_details_page.get_dob()
        assert employee_data['yob'] in personal_details_page.get_dob()
