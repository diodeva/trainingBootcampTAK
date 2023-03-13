import unittest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Edge(EdgeChromiumDriverManager().install())


    # def test_failed_login(self):
    #     driver = self.browser
    #     driver.get("https://demowebshop.tricentis.com/")
    #     driver.find_element(By.CLASS_NAME, "ico-login").click()
    #     driver.find_element(By.ID, "Email").send_keys("superQA000@gmail.com")
    #     driver.find_element(By.ID, "Password").send_keys("super123")
    #     driver.find_element(By.CLASS_NAME, "button-1.login-button").click()

    #     data = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
    #     self.assertIn("Login was unsuccessful. Please correct the errors and try again.", data)
    #     driver.minimize_window()


    # def test_empty_username(self):
    #     driver = self.browser
    #     driver.get("https://demowebshop.tricentis.com/")
    #     driver.find_element(By.CLASS_NAME, "ico-login").click()
    #     driver.find_element(By.ID, "Email").send_keys("")
    #     driver.find_element(By.ID, "Password").send_keys("super123")
    #     driver.find_element(By.CLASS_NAME, "button-1.login-button").click()
    #     data = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
    #     self.assertIn("Login was unsuccessful. Please correct the errors and try again.\nNo customer account found", data)
    #     driver.minimize_window()

    # def test_empty_password(self):
    #     driver = self.browser
    #     driver.get("https://demowebshop.tricentis.com/")
    #     driver.find_element(By.CLASS_NAME, "ico-login").click()
    #     driver.find_element(By.ID, "Email").send_keys("superQA@gmail.com")
    #     driver.find_element(By.ID, "Password").send_keys("")
    #     driver.find_element(By.CLASS_NAME, "button-1.login-button").click()
    #     data = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
    #     self.assertIn("Login was unsuccessful. Please correct the errors and try again.\nThe credentials provided are incorrect", data)
    #     driver.minimize_window()

    # def test_wrong_format_email(self):
    #     driver = self.browser
    #     driver.get("https://demowebshop.tricentis.com/")
    #     driver.find_element(By.CLASS_NAME, "ico-login").click()
    #     driver.find_element(By.ID, "Email").send_keys("superQAgmail.com")
    #     driver.find_element(By.ID, "Password").send_keys("super123")
    #     driver.find_element(By.CLASS_NAME, "button-1.login-button").click()
    #     verify = driver.find_element(By.CLASS_NAME, "field-validation-error").text
    #     self.assertIn("Please enter a valid email address.", verify)
    #     driver.minimize_window()

    def test_failed_recovery(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.CLASS_NAME, "forgot-password").click()
        driver.find_element(By.ID, "Email").send_keys("superQA@mailto.com")
        driver.find_element(By.NAME, "send-email").click()

    def test_success_recovery(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.CLASS_NAME, "forgot-password").click()
        driver.find_element(By.ID, "Email").send_keys("superQA@gmail.com")
        driver.find_element(By.NAME, "send-email").click()
        
    def test_success_login(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys("superQA@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("super123")
        driver.find_element(By.CLASS_NAME, "button-1.login-button").click()


    def tearDown(self):
        self.browser.close()
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()