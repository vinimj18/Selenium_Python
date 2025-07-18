# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from page_objects.login_page import LoginPage
# import time


# @pytest.fixture
# def setup_browser():
#     service = Service('chromedriver/chromedriver.exe')
#     driver = webdriver.Chrome(service=service)
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     yield driver
#     driver.quit()


# def test_login(setup_browser, self):
#     driver = setup_browser
#     driver.get('https://opensource-demo.orangehrmlive.com/')

#     login_page = LoginPage(self.driver)
#     login_page.enter_user().send_keys("Admin")

#     driver.find_element(By.NAME, 'password').send_keys('admin123')
#     driver.find_element(By.CLASS_NAME, 'orangehrm-login-button').click()
#     header = driver.find_element(By.CLASS_NAME, 'oxd-topbar-header-title')
#     menu = driver.find_element(By.CLASS_NAME, 'oxd-main-menu')
#     dashboard_card = driver.find_element(
#         By.CLASS_NAME, 'orangehrm-dashboard-widget')
#     assert header.is_displayed()
#     assert menu.is_displayed()
#     assert dashboard_card.is_displayed()


def test_add_new_employee(setup_browser):

    test_login(setup_browser)
    driver = setup_browser
    wait = WebDriverWait(driver, 5)

    driver.find_elements(
        By.CLASS_NAME, 'oxd-main-menu-item')[1].click()
    driver.find_elements(
        By.CLASS_NAME, 'oxd-topbar-body-nav-tab-item')[2].click()
    driver.find_element(By.NAME, 'firstName').send_keys('Vinicius')
    driver.find_element(By.NAME, 'lastName').send_keys('Justen')
    employee_id = driver.find_element(
        By.CSS_SELECTOR, "div[class='oxd-input-group oxd-input-field-bottom-space'] div input[class='oxd-input oxd-input--active']").get_attribute('value')
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    pop_up = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'p.oxd-text.oxd-text--p.oxd-text--toast-message.oxd-toast-content-text')))
    assert "Successfully" in pop_up.text
    assert driver.find_element(By.NAME, 'firstName').get_attribute(
        'value') == 'Vinicius'
    assert driver.find_element(By.NAME, 'lastName').get_attribute(
        'value') == 'Justen'

    assert driver.find_elements(
        By.CSS_SELECTOR, 'input.oxd-input.oxd-input--active')[4].get_attribute('value') == employee_id

    return employee_id

    # Test 3.1: Search for Employee by Name


def test_search_employee_by_name(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 5)
    employee_id = test_add_new_employee(setup_browser)

    driver.find_elements(
        By.CLASS_NAME, 'oxd-main-menu-item')[1].click()

    driver.find_element(
        By.CSS_SELECTOR, "input[placeholder='Type for hints...']").send_keys('Vinicius Justen')

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    row = driver.find_element(
        By.XPATH, f"//div[@class='oxd-table-card']//div[contains(text(), {employee_id})]")
    cells = row.find_elements(By.CLASS_NAME, "oxd-table-cell")

    assert cells[0].text == employee_id
    assert cells[1].text == "Vinicius"
    assert cells[2].text == "Justen"


def test_search_employee_by_id(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 5)
    employee_id = test_add_new_employee(setup_browser)

    driver.find_elements(
        By.CLASS_NAME, 'oxd-main-menu-item')[1].click()

    driver.find_element(
        By.CSS_SELECTOR, "input[placeholder='Type for hints...']").send_keys(employee_id)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    row = driver.find_element(
        By.XPATH, f"//div[@class='oxd-table-card']//div[contains(text(), {employee_id})]")
    cells = row.find_elements(By.CLASS_NAME, "oxd-table-cell")

    assert cells[0].text == employee_id
    assert cells[1].text == "Vinicius"
    assert cells[2].text == "Justen"


# def test_update_employee_info(setup_browser):
#     driver = setup_browser
#     wait = WebDriverWait(driver, 5)

#     test_search_employee_by_name(setup_browser)

    # o Edit the employee profile
    # Locate Pencil button -> Click
    # Implicit Wait
    # o Update fields Nationality and Date of Birth
    # Locate Nationality Field -> Insert Italian
    # Locate Date of Birth Field -> Insert 1988-18-07
    # Locate Save Button -> Click
    # Implicit Wait
    # o Assert that the changes are saved and displayed
    # Refresh
    # Locate Nationality Field -> Assert Italian
    # Locate Date of Birth Field -> Assert 1988-18-07
