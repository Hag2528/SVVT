import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# If you want to import a module called solve
import solve
# Or if you want to import a specific function from a module
# from some_module import solve
import os
import time

class ContractRenewalSystemTest(unittest.TestCase):
    """Test cases for Contract Renewal System UI"""
    
    def setUp(self):
        """Set up test environment before each test"""
        # Check if we should take screenshots
        self.take_screenshots = os.environ.get('TAKE_SCREENSHOTS', 'False').lower() == 'true'
        self.screenshots_dir = os.environ.get('SCREENSHOTS_DIR', 'test_reports/screenshots')
        
        # Create screenshots directory if needed
        if self.take_screenshots and not os.path.exists(self.screenshots_dir):
            os.makedirs(self.screenshots_dir)
        
        # Initialize WebDriver
        self.driver = webdriver.Chrome()  # Use Chrome driver
        self.driver.maximize_window()
        self.base_url = "http://localhost:8000"  # Update with your application URL
        self.wait = WebDriverWait(self.driver, 10)  # 10 seconds timeout
    
    def tearDown(self):
        """Clean up after each test"""
        if self.driver:
            self.driver.quit()
    
    def take_screenshot(self, name):
        """Take a screenshot if enabled"""
        if self.take_screenshots:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"{self.screenshots_dir}/{name}_{timestamp}.png"
            self.driver.save_screenshot(filename)
            print(f"Screenshot saved: {filename}")
            return filename
        return None
    
    def test_01_login_page_elements(self):
        """Test login page UI elements"""
        self.driver.get(f"{self.base_url}/login/")
        
        # Take screenshot of login page
        self.take_screenshot("01_login_page")
        
        # Check page title
        self.assertIn("Login", self.driver.title)
        
        # Check for username field
        username_field = self.driver.find_element(By.NAME, "username")
        self.assertTrue(username_field.is_displayed())
        
        # Check for password field
        password_field = self.driver.find_element(By.NAME, "password")
        self.assertTrue(password_field.is_displayed())
        
        # Check for login button
        login_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        self.assertTrue(login_button.is_displayed())
        
        # Take screenshot with fields highlighted
        self.take_screenshot("01_login_page_elements")
    
    def test_02_invalid_login(self):
        """Test invalid login attempt"""
        self.driver.get(f"{self.base_url}/login/")
        
        # Enter invalid credentials
        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys("invalid_user")
        
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("invalid_password")
        
        # Take screenshot before submitting
        self.take_screenshot("02_invalid_login_before")
        
        # Click login button
        login_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        login_button.click()
        
        # Wait for error message
        try:
            error_message = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
            )
            self.assertTrue(error_message.is_displayed())
            self.take_screenshot("02_invalid_login_error")
        except TimeoutException:
            self.take_screenshot("02_invalid_login_timeout")
            self.fail("Error message not displayed after invalid login")
    
    def test_03_valid_login(self):
        """Test valid login attempt"""
        self.driver.get(f"{self.base_url}/login/")
        
        # Enter valid credentials (update with valid test credentials)
        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys("testuser")
        
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("testpass123")
        
        # Take screenshot before submitting
        self.take_screenshot("03_valid_login_before")
        
        # Click login button
        login_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        login_button.click()
        
        # Wait for dashboard to load
        try:
            dashboard_element = self.wait.until(
                EC.presence_of_element_located((By.ID, "dashboard"))
            )
            self.assertTrue(dashboard_element.is_displayed())
            self.take_screenshot("03_valid_login_dashboard")
        except TimeoutException:
            self.take_screenshot("03_valid_login_timeout")
            self.fail("Dashboard not displayed after valid login")

# Add more test methods as needed


if __name__ == "__main__":
    unittest.main()


