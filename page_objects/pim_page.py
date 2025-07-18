from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMPage:

    def __init__(self, driver) -> None:
        self.driver = driver

    add_employee = (By.CLASS_NAME, 'oxd-topbar-body-nav-tab-item')
    employee_name = (By.CSS_SELECTOR, "input[placeholder='Type for hints...']")
    search_button = (By.CSS_SELECTOR, "button[type='submit']")
    results = (By.CSS_SELECTOR, "div[role='rowgroup'] div[role='row']")
    cells = (By.CSS_SELECTOR, "div.oxd-table-cell")

    def get_add_employee_button(self):
        return self.driver.find_elements(*PIMPage.add_employee)[2]

    def get_employee_name_field(self):
        return self.driver.find_elements(*PIMPage.employee_name)[0]

    def get_search_button(self):
        return self.driver.find_element(*PIMPage.search_button)

    def wait_results(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(PIMPage.results))

    def get_result(self, employee_id):
        return self.driver.find_element(By.XPATH, f"//div[@role='rowgroup']//div[contains(text(), '{employee_id}')]/ancestor::div[@role='row']")

    def get_cells(self, row):
        return self.driver.find_elements(*PIMPage.cells)
