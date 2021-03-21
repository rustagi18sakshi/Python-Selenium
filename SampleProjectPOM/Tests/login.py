from selenium import webdriver
import time
import unittest
# For running from command line we need to add below mentioned libraries.
# Otherwise error received : ImportError: No module named SampleProjectPOM.Pages.loginPage
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SampleProjectPOM.Pages.loginPage import LoginPage
from SampleProjectPOM.Pages.homePage import HomePage
import HtmlTestRunner

class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):                       # Similar to @BeforeClass in TestNG
        cls.driver = webdriver.Chrome("../../drivers/chromedriver/chromedriver.exe")
        cls.driver.implicitly_wait(10)         # Applying implicit wait of 10 sec
        cls.driver.maximize_window()           # For maximising window

    def test_01login_valid_username(self):
        # Assigning this for simplicity so that we can directly access using driver in next steps
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)              # Creating object for LoginPage class
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homePage = HomePage(driver)            # Creating object for HomePage class
        homePage.click_welcome()
        homePage.click_logout()

        time.sleep(2)

    def test_02login_invalid_username(self):
        # Assigning this for simplicity so that we can directly access using driver in next steps
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)              # Creating object for LoginPage class
        login.enter_username("Admin1")         # Providing invalid username
        login.enter_password("admin123")
        login.click_login()
        message = login.check_invalid_username_message()
        self.assertEqual(message, "Invalid credentials")

    @classmethod
    def tearDownClass(cls):                    # Similar to @AfterClass in TestNG
        cls.driver.close()
        cls.driver.quit()
        print "Test completed"

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../../reports"))