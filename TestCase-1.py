# TestCase - 1
# Open Web Browser(Chrome/Firefox/IE)
# Open URL https://admin-demo.nopcommerce.com/login
# Provide Email (admin@yourstore.com)
# Provide password(admin)
# Click on Login
# Capture title of the Dashboard page(Actual Title)
# Verify title of the page: "Dashboard / nopcommerce administration" (Expected)
# Close browser

import time
from selenium import webdriver # webdriver is a module available in Selenium package
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# webdriver-manager should be installed via settings.
driver=webdriver.Chrome(ChromeDriverManager().install())
# This will automatically install the browserdrivers. so, versioning problem can be overcomed.

# This is used to stop the auto closure of chrome window after the script is executed.
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
# service_obj = Service("E:\Automation\Drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service = service_obj,options = chrome_options)

# driver = webdriver.Chrome(executable_path="E:\Automation\Drivers\chromedriver_win32\chromedriver.exe")
#driver is a object = webdriver is a module.Chrome() is a class. executable_path is optional(It defines the keyword argument).
#Chrome is a constructor with browser driver parameters. It expects the location of the browser driver.

#Lauching chrome without mentioning the driver path
# Put the drivers in this path, "C:\Users\Reshma S\AppData\Local\Programs\Python\Python39\Scripts"
# driver = webdriver.Chrome()
# -------------------------------------------------------------------------------------------------------------------------------------

# Selenium 4
# Depricated warning, According to Selenium4,
# serv_obj = Service(executable_path="E:\Automation\Drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service = serv_obj)

driver = webdriver.Chrome()

driver.get("https://admin-demo.nopcommerce.com/login")

email = driver.find_element(By.ID, "Email")
email.clear()
email.send_keys("admin@yourstore.com")

password = driver.find_element(By.ID, "Password")
password.clear()
password.send_keys("admin")

loginbutton = driver.find_element(By.XPATH, "//button[@class='button-1 login-button']")
loginbutton.click()

expectedtitle = "Dashboard / nopCommerce administration"
actualtitle = driver.title

if expectedtitle == actualtitle:
    print("Captured Title is "+actualtitle)
else:
    print("Title Not Captured")

driver.close()