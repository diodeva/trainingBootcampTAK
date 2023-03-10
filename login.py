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


    def test_failed_login(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys("superQA000@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("super123")
        driver.find_element(By.CLASS_NAME, "button-1.login-button").click()


    def test_empty_username(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys("")
        driver.find_element(By.ID, "Password").send_keys("super123")
        driver.find_element(By.CLASS_NAME, "button-1.login-button").click()

    def test_empty_password(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys("superQA@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("")
        driver.find_element(By.CLASS_NAME, "button-1.login-button").click()

    def test_wrong_format_email(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys("superQAgmail.com")
        driver.find_element(By.ID, "Password").send_keys("super123")
        driver.find_element(By.CLASS_NAME, "button-1.login-button").click()

    def test_failed_recovery(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.CLASS_NAME, "forgot-password").click()
        driver.find_element(By.ID, "Email").send_keys("superQA@mailto.com")
        
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="send-email"].button-1.password-recovery-button')))
        button.click()
        # driver.find_element(By.CSS_SELECTOR, 'input[name="send-email"].button-1.password-recovery-button').click()


    def test_success_recovery(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.CLASS_NAME, "forgot-password").click()
        driver.find_element(By.ID, "Email").send_keys("superQA@gmail.com")

        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="send-email"].button-1.password-recovery-button')))
        button.click()
        # driver.find_element(By.CSS_SELECTOR, 'input[name="send-email"].button-1.password-recovery-button').click()

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