from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewEmployeePage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    # Locators
    first_name = (By.NAME, 'firstName')
    last_name = (By.NAME, 'lastName')
    employee_id = (
        By.CSS_SELECTOR, "div[class='oxd-input-group oxd-input-field-bottom-space'] div input[class='oxd-input oxd-input--active']")
    save_button = (By.CSS_SELECTOR, "button[type='submit']")
    pop_up = (By.CSS_SELECTOR,
              'p.oxd-text.oxd-text--p.oxd-text--toast-message.oxd-toast-content-text')

    # Elements
    def get_first_name(self):
        return self.driver.find_element(*NewEmployeePage.first_name)

    def get_last_name(self):
        return self.driver.find_element(*NewEmployeePage.last_name)

    def get_employee_id(self):
        return self.driver.find_element(*NewEmployeePage.employee_id)

    def get_save_button(self):
        return self.driver.find_element(*NewEmployeePage.save_button)

    def get_pop_up(self):
        return self.wait.until(EC.visibility_of_element_located(NewEmployeePage.pop_up))
