from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
import os

chrome_option = webdriver.EdgeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(EdgeChromiumDriverManager().install()), options = chrome_option)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


# Method - 1:
# path\name with extension
# driver.save_screenshot("E:\\Automation\\Practice_Selenium\\ss.png")

# Also can write like,
# driver.save_screenshot(os.getcwd()+"\\ss.png")

# Method - 2:
# driver.get_screenshot_as_file(os.getcwd()+"\\ss.png")

# Method - 3:
driver.get_screenshot_as_base64() # This will return in a binary format
driver.get_screenshot_as_png() # This will return in a encoded format