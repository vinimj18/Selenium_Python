import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def setup_browser():
    service = Service('chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login(setup_browser):
    driver = setup_browser
    driver.get('https://opensource-demo.orangehrmlive.com/')
    time.sleep(2)  # Wait for the page to load
    driver.find_element(By.NAME, 'username').send_keys('Admin')
    driver.find_element(By.NAME, 'password').send_keys('admin123')
    driver.find_element(By.CLASS_NAME, 'orangehrm-login-button').click()
    time.sleep(15)  # Wait for the page to load
    dropdown = driver.find_element(By.CLASS_NAME, 'oxd-userdropdown-name')
    assert (dropdown.is_displayed())

# def test_add_new_employee(setup_browser):
