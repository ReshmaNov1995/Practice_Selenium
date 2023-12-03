"""
launch the chrome
navigate to google.com
Enter any name in search
click on the search
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service = Service(EdgeChromiumDriverManager().install()))

driver.get("www.google.com/")
driver.maximize_window()

name = driver.find_element(By.CLASS_NAME, "gLFyf")
search = driver.find_element(By.XPATH, "//input[@class='gNO89b']")
search.click()