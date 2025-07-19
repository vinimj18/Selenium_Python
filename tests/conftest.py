import pytest

from selenium import webdriver

driver = None


@pytest.fixture(scope='class')
def setup(request):
    global driver
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/')

    request.cls.driver = driver

    yield driver
    driver.quit()
