import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Test case to verify Google page opens
@pytest.mark.usefixtures("setup")
def test_google_page_open():
    driver = open_google()

    # Check if the title contains "Google"
    assert "Google" in driver.title, f"Expected title to contain 'Google', but got '{driver.title}'"

    # Close the driver after test completion
    driver.quit()

# Fixture to set up WebDriver
@pytest.fixture(scope="function")
def setup():
    # Initialize WebDriver before each test
    global driver
    driver = webdriver.Chrome()
    yield
    driver.quit()
