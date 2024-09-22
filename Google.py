from selenium import webdriver
from selenium.webdriver.common.by import By

# Function to open Google
def open_google():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.google.com")
    return driver
