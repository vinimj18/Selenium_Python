from page_objects.login_page import LoginPage
from page_objects.dashboard_page import DashboardPage
from test_data.login_credentials import login_credentials

import pytest


@pytest.mark.usefixtures('setup')
class TestLogin:

    @pytest.mark.parametrize('credentials', login_credentials)
    def test_login(self, setup, credentials):
        driver = setup
        login_page = LoginPage(driver)

        login_page.login(credentials)

        dashboard_page = DashboardPage(driver)

        assert dashboard_page.get_header().is_displayed()
        assert dashboard_page.get_menu().is_displayed()
        assert dashboard_page.get_card().is_displayed()
