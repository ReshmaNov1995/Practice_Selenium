from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option("detach", True)

driver = webdriver.Edge()

driver.get("https://accounts.google.com/signup/v2/createaccount?theme=glif&flowName=GlifWebSignIn&flowEntry=SignUp")

driver.find_element(By.ID, "firstName").send_keys("Reshma")
driver.find_element(By.XPATH,"//input[@name='lastName']").send_keys("S")
driver.find_element(By.XPATH, "//div[@class='zQJV3']/descendant::div[7]/following::span[1]").click()

