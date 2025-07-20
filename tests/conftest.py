import pytest
from selenium import webdriver

driver = None

# Initial WebDriver Configuration


@pytest.fixture(scope='class')
def setup(request):
    global driver

    # Sets the webdriver to run on Google Chrome
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)

    # Sets standard timeout
    driver.implicitly_wait(10)

    # Runs the tests in a maximized window
    driver.maximize_window()

    # Sets the project's BaseURL
    driver.get('https://opensource-demo.orangehrmlive.com/')

    request.cls.driver = driver

    # Waits for the tests to run
    yield driver

    # Closes the driver once the tests are finished
    driver.quit()
