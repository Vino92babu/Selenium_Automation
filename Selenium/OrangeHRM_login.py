from selenium import webdriver
driver = webdriver.Chrome("C:\Python3.9.10\Scripts\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element_by_name("username").send_keys("Vino")
