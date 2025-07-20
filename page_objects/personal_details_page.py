from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PersonalDetailsPage:

    def __init__(self, driver) -> None:
        self.driver = driver

    # Locators
    nationality_arrow = (By.CLASS_NAME, 'oxd-select-text--arrow')
    nationality_dropdown = (By.CSS_SELECTOR, "div[role='listbox'] > div")
    nationality_text = (By.CLASS_NAME, "oxd-select-text-input")
    calendar_open = (By.CLASS_NAME, 'oxd-date-input-icon')
    calendar_dropdown = (By.CLASS_NAME, 'oxd-icon-button__icon')
    day_options = (By.CLASS_NAME, 'oxd-calendar-date')
    month_options = (By.CLASS_NAME, 'oxd-calendar-dropdown--option')
    year_options = (By.CLASS_NAME, 'oxd-calendar-dropdown--option')
    save_button = (By.CSS_SELECTOR, "button[type='submit']")
    dob_text = (By.CSS_SELECTOR, "input[data-v-4a95a2e0]")

    # Elements
    def open_nationality_dd(self):
        return self.driver.find_elements(*PersonalDetailsPage.nationality_arrow)[0]

    def open_dob_calendar(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(PersonalDetailsPage.calendar_open))
        return self.driver.find_elements(*PersonalDetailsPage.calendar_open)[1]

    def get_month(self):
        return self.driver.find_elements(*PersonalDetailsPage.calendar_dropdown)[0]

    def get_year(self):
        return self.driver.find_elements(*PersonalDetailsPage.calendar_dropdown)[1]

    def get_save_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(PersonalDetailsPage.save_button))
        return self.driver.find_element(*PersonalDetailsPage.save_button)

    def get_nationality(self):
        return self.driver.find_element(*PersonalDetailsPage.nationality_text).text

    def get_dob(self):
        element = self.driver.find_elements(*PersonalDetailsPage.dob_text)[1]
        return element.get_attribute('value') or element.text
