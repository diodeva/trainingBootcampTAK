import unittest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestCart(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Edge(EdgeChromiumDriverManager().install())


    def test_success_add_item(self):
        # driver = self.browser
        # driver.get("https://demowebshop.tricentis.com/")
        # driver.find_element(By.CLASS_NAME, "ico-login").click()
        # driver.find_element(By.ID, "Email").send_keys("superQA@gmail.com")
        # driver.find_element(By.ID, "Password").send_keys("super123")
        # driver.find_element(By.CLASS_NAME, "button-1.login-button").click()
        # driver.find_element(By.)

    def test_success_remove_item(self):
        # driver = self.browser
        # driver.get("https://demowebshop.tricentis.com/")
        # driver.find_element(By.CLASS_NAME, "ico-login").click()
        # driver.find_element(By.ID, "Email").send_keys("superQA@gmail.com")
        # driver.find_element(By.ID, "Password").send_keys("super123")
        # driver.find_element(By.CLASS_NAME, "button-1.login-button").click()

    def test_wrong_format_email(self):
        # driver = self.browser
        # driver.get("https://demowebshop.tricentis.com/")
        # driver.find_element(By.CLASS_NAME, "ico-login").click()
        # driver.find_element(By.ID, "Email").send_keys("")
        # driver.find_element(By.ID, "Password").send_keys("super123")
        # driver.find_element(By.CLASS_NAME, "button-1.login-button").click()

    def test_success_checkout(self):
        # driver = self.browser
        # driver.get("https://demowebshop.tricentis.com/")
        # driver.find_element(By.CLASS_NAME, "ico-login").click()
        # driver.find_element(By.ID, "Email").send_keys("superQAgmailcom")
        # driver.find_element(By.ID, "Password").send_keys("super123")
        # driver.find_element(By.CLASS_NAME, "forgot-password").click()
        # driver.find_element(By.ID, "Email").send_keys("superQA@mailto.com")
        # driver.find_element(By.CSS_SELECTOR, 'input[name="send-email"].button-1.password-recovery-button').click()

    def test_success_empty_cart(self):
        # driver = self.browser
        # driver.get("https://demowebshop.tricentis.com/")
        # driver.find_element(By.CLASS_NAME, "ico-login").click()
        # driver.find_element(By.ID, "Email").send_keys("superQA@gmail.com")
        # driver.find_element(By.ID, "Password").send_keys("")
        # driver.find_element(By.CLASS_NAME, "forgot-password").click()
        # driver.find_element(By.ID, "Email").send_keys("superQA@gmail.com")
        # driver.find_element(By.CSS_SELECTOR, 'input[name="send-email"].button-1.password-recovery-button').click()


    def tearDown(self):
        self.browser.close()
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()