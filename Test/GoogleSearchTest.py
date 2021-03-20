from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import unittest

class GoogleSearch(unittest.TestCase):

    def setUpClass(cls):
        cls.driver = webdriver.Chrome("..\drivers\chromedriver\chromedriver.exe")
        cls.driver.implicitly_wait(10)         # Applying implicit wait of 10 sec
        cls.driver.maximize_window()           # For maximising window

    def test_search_automationStepByStep(self):
        self.driver.get("http://google.com")                                           # Opening browser
        self.driver.find_element_by_name("q").send_keys("Automation step by step")     # Performing search operation
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)

    def test_search_sakshi(self):
        self.driver.get("http://google.com")                                           # Opening browser
        self.driver.find_element_by_name("q").sen   d_keys("Sakshi")                      # Performing search operation
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)

    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print "Test completed"


