from selenium import webdriver
import pytest

# pytest fixture defines the test Setup and teardown(as yield) which can be run in tests that want to you these
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome("../drivers/chromedriver/chromedriver.exe")
    driver.implicitly_wait(10)  # Applying implicit wait of 10 sec
    driver.maximize_window()    # For maximising window
    yield                       # Teardown steps added here
    driver.close()
    driver.quit()
    print "Test completed"

# We need to pass test Set up function name "test_setup" in the tests where we want to run Setup
def test_login(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    title = driver.title
    assert title == "OrangeHRM"