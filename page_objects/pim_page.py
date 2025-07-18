from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMPage:

    def __init__(self, driver) -> None:
        self.driver = driver

    add_employee = (By.CLASS_NAME, 'oxd-topbar-body-nav-tab-item')
    employee_img = (By.CLASS_NAME, 'employee-image')

    def get_add_employee_button(self):
        return self.driver.find_elements(*PIMPage.add_employee)[2]

    def get_current_url(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.url_changes(self.driver.current_url))
