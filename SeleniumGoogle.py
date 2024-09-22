from selenium import webdriver
from selenium.webdriver.common.by import By

# Function to open Google
def open_google():
    # Initialize WebDriver (assuming you're using Chrome)
    driver = webdriver.Chrome()

    # Open Google
    driver.get("https://www.google.com")

    # Return the driver object for further interactions
    return driver
