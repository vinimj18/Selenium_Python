from utils.base_class import BaseClass
from page_objects.login_page import LoginPage
from page_objects.dashboard_page import DashboardPage
from test_data.test_data import data


class TestLogout(BaseClass):
    def test_logout(self):

        # Test Navigation
        self.login(data['login']['username'],
                   data['login']['password'])

        dashboard_page = DashboardPage(self.driver)
        dashboard_page.get_dropdown_arrow().click()
        dashboard_page.get_logout_link().click()

        login_page = LoginPage(self.driver)

        # Test Assertions
        assert login_page.get_login_button().is_displayed()
