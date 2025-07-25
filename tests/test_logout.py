from utils.base_class import BaseClass
from page_objects.login_page import LoginPage
from page_objects.dashboard_page import DashboardPage
from test_data.login_credentials import login_credentials

import pytest


class TestLogout(BaseClass):

    def test_logout(self):
        self.login(login_credentials['username'],
                   login_credentials['password'])

        dashboard_page = DashboardPage(self.driver)
        dashboard_page.get_dropdown_arrow().click()
        dashboard_page.get_logout_link().click()

        login_page = LoginPage(self.driver)
        assert login_page.get_login_button().is_displayed()
