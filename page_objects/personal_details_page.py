from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PersonalDetailsPage:

    def __init__(self, driver) -> None:
        self.driver = driver

    nationality_arrow = (By.CLASS_NAME, 'oxd-select-text--arrow')
    nationality_dropdown = (By.CSS_SELECTOR, "div[role='listbox'] > div")
    calendar_open = (By.CLASS_NAME, 'oxd-date-input-icon')
    month_selector = (By.CLASS_NAME, 'oxd-calendar-selector-month-selected')
    year_selector = (By.CLASS_NAME, 'oxd-calendar-selector-year-selected')
    calendar_dropdown = (By.CLASS_NAME, 'oxd-calendar-dropdown')
    calendar = (By.CLASS_NAME, 'oxd-calendar-wrapper')
    save_button = (
        By.CSS_SELECTOR, "div[class='orangehrm-horizontal-padding orangehrm-vertical-padding'] button[type='submit']")
    nationality_text = (By.CLASS_NAME, "oxd-select-text-input")
    dob_text = (By.CSS_SELECTOR, "div.oxd-date-input input.oxd-input")

    def open_nationality_dd(self):
        return self.driver.find_elements(*PersonalDetailsPage.nationality_arrow)[0]

    def open_dob_calendar(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(PersonalDetailsPage.calendar_open))
        return self.driver.find_elements(*PersonalDetailsPage.calendar_open)[1]

    def get_day(self, day):
        xpath = f"//div[contains(@class, 'oxd-calendar-date-wrapper')]//div[text()='{day}']"
        return self.driver.find_element(By.XPATH, xpath)

    def get_month(self):
        return self.driver.find_element(*PersonalDetailsPage.month_selector)

    def get_year(self):
        return self.driver.find_element(*PersonalDetailsPage.year_selector)

    def get_save_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(PersonalDetailsPage.calendar))
        return self.driver.find_element(*PersonalDetailsPage.save_button)

    def get_nationality(self):
        return self.driver.find_element(*PersonalDetailsPage.nationality_text).text

    def get_dob(self):
        element = self.driver.find_element(*PersonalDetailsPage.dob_text)
        return element.get_attribute('value') or element.text
