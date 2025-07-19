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
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((PIMPage.results)))

    def search_employee(self, first_name, last_name, employee_id):
        self.get_employee_name_field().send_keys(
            f'{first_name} {last_name}')
        self.get_search_button().click()
        self.wait_results()
        return self.get_row_by_employee_id(employee_id)

    def get_row_by_employee_id(self, employee_id):
        xpath = f"//div[@role='rowgroup']//div[(text()='{employee_id}')]/ancestor::div[@role='row']"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        return self.driver.find_element(By.XPATH, xpath)

    def get_cells_by_employee_id(self, employee_id):
        row = self.get_row_by_employee_id(employee_id)
        return row.find_elements(*PIMPage.cells)

    def wait_for_id_tobe_clickable(self, employee_id):
        xpath = f"//div[@role='rowgroup']//div[(text()='{employee_id}')]/ancestor::div[@role='row']"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, xpath)))
