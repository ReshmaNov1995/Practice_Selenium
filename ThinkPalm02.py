"""
scroll down and click action
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option("detach", True)

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_option)

driver.get("https://support.google.com/mail/answer/56256?hl=en")
driver.maximize_window()

element = driver.find_element(By.XPATH, "//div[@class='language-selector-select sc-select']")
scroll = driver.execute_script("arguments[0].scrollIntoView();",element)
# scroll1 = driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
element.click()