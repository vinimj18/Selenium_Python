from utils.base_class import BaseClass
from page_objects.dashboard_page import DashboardPage
from test_data.login_credentials import login_credentials

import pytest


class TestLogin(BaseClass):

    def test_login(self):
        self.login(login_credentials['username'],
                   login_credentials['password'])

        dashboard_page = DashboardPage(self.driver)

        assert dashboard_page.get_header().is_displayed()
        assert dashboard_page.get_menu().is_displayed()
        assert dashboard_page.get_card().is_displayed()
