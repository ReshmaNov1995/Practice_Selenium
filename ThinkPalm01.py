"""
take the screenshot
"""

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option("detach", True)

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_option)
driver.get("https://support.google.com/mail/answer/56256?hl=en")
driver.save_screenshot("E:\\New folder (2)\\gmailscreenshot.png")

