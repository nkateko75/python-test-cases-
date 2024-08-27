from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (Make sure to have the appropriate driver installed)
driver = webdriver.Chrome()

# Test Case 1: Verify Page Title
def test_verify_page_title():
    driver.get("https://rkmabundattorneysinc.co.za/Contact%20us.html")  # Update with the correct path
    assert driver.title == "Contact Us"

# Run the tests
if __name__ == "__main__":
    test_verify_page_title()
   
    # Close the browser
    driver.quit()
