from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option("detach", True)

driver = webdriver.Edge(service = Service(EdgeChromiumDriverManager().install()), options = edge_option)

driver.get("https://www.foundit.in/")
driver.maximize_window()

driver.find_element(By.XPATH, "//div[@class='heroSection-buttonContainer_secondaryBtn__text']").click()
driver.find_element(By.XPATH, "//input[@id='file-upload']").send_keys("C:\\Users\\Reshma S\\Downloads\\Export - 2023-03-17T191519.716.pdf")