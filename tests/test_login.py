from utils.base_class import BaseClass
from page_objects.dashboard_page import DashboardPage
from test_data.test_data import data


class TestLogin(BaseClass):
    def test_login(self):

        # Test Navigation
        self.login(data['login']['username'],
                   data['login']['password'])

        dashboard_page = DashboardPage(self.driver)

        # Test Assertions
        assert dashboard_page.get_header().is_displayed()
        assert dashboard_page.get_menu().is_displayed()
        assert dashboard_page.get_card().is_displayed()
