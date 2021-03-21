from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner

# To install html reporter : pip install html-testRunner

class GoogleSearchHTMLReport(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../drivers/chromedriver/chromedriver.exe")
        cls.driver.implicitly_wait(10)         # Applying implicit wait of 10 sec
        cls.driver.maximize_window()           # For maximising window

    def test_search_automationStepByStep(self):
        self.driver.get("http://google.com")                                           # Opening browser
        self.driver.find_element_by_name("q").send_keys("Automation step by step")     # Performing search operation
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)

    def test_search_sakshi(self):
        self.driver.get("http://google.com")                                           # Opening browser
        self.driver.find_element_by_name("q").send_keys("Sakshi")                      # Performing search operation
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print "Test completed"

# To run this test from command line : Go to directory and run command : python -m unittest GoogleSearchTest.py
# If we want to run it directly using : python GoogleSearchTest.py, then we need to add below code in our testcase.

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../reports"))       # For reporting


