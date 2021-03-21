from selenium import webdriver

def test_setup():
    global driver
    driver = webdriver.Chrome("../drivers/chromedriver/chromedriver.exe")
    driver.implicitly_wait(10)  # Applying implicit wait of 10 sec
    driver.maximize_window()    # For maximising window

def test_login():
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    title = driver.title
    assert title == "OrangeHRM"

def test_teardown():
    driver.close()
    driver.quit()
    print "Test completed"