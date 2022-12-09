from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()

# ID
# serachfield = driver.find_element(By.ID, "small-searchterms")
# NAME
serachfield = driver.find_element(By.NAME, "q")
serachfield.send_keys("lenovo-thinkpad-x1-carbon-laptop")


searchbutton = driver.find_element(By.XPATH, "//button[@class='button-1 search-box-button']")
searchbutton.click()

# LINKTEXT
# registerbutton = driver.find_element(By.LINK_TEXT, "Register").click()
# PARTIALLINKTEXT
registerbutton = driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()
