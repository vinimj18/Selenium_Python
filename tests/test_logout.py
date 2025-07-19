from page_objects.login_page import LoginPage
from page_objects.dashboard_page import DashboardPage
from test_data.login_credentials import login_credentials

import pytest


@pytest.mark.usefixtures('setup')
class TestLogout:

    def test_logout(self, setup):
        driver = setup

        login_page = LoginPage(driver)
        login_page.login(
            login_credentials['username'], login_credentials['password'])

        dashboard_page = DashboardPage(driver)
        dashboard_page.get_dropdown_arrow().click()
        dashboard_page.get_logout_link().click()

        assert login_page.get_login_button().is_displayed()
