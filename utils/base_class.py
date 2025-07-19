import pytest

from page_objects.login_page import LoginPage


@pytest.mark.usefixtures('setup')
class BaseClass:
    driver = None

    def login(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.enter_user().send_keys(username)
        login_page.enter_password().send_keys(password)
        login_page.get_login_button().click()
