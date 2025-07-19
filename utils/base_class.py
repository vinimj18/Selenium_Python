import pytest

from page_objects.login_page import LoginPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures('setup')
class BaseClass:

    driver = None

    # def __init__(self, driver) -> None:
    #     self.driver = driver

    def login(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.enter_user().send_keys(username)
        login_page.enter_password().send_keys(password)
        login_page.get_login_button().click()

    def drop_down_selection(self, arrow_element, dropdown_locator, value):
        arrow_element.click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(dropdown_locator))
        options = self.driver.find_elements(*dropdown_locator)

        for option in options:
            if option.text.strip() == value:
                option.click()
                break
