from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.flipkart.com/")

driver.maximize_window()

driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']").click()

# CLASSNAME
slide = driver.find_elements(By.CLASS_NAME, "eFQ30H")
print(len(slide))


# TAGNAME
link = driver.find_elements(By.TAG_NAME, "a")
print(len(link))