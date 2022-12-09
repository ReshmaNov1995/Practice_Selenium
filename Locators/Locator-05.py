from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

# Register button
# Absolute Xpath
# driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/ul/li[1]/a").click()

# Relative Xpath
# driver.find_element(By.XPATH, "//div[@class='header-links']/ul/li[1]/a").click()

# and
# driver.find_element(By.XPATH, "//input[@class='search-box-text ui-autocomplete-input' and @id='small-searchterms']").send_keys("laptop")

# or
# driver.find_element(By.XPATH, "//button[@type='submit' or @class='button-1 search-box-button']").click()

# contains
driver.find_element(By.XPATH, "//input[contains(@id,'searchterms')]").send_keys("laptop")

# starts-with
# driver.find_element(By.XPATH, "//button[starts-with(@class,'button-1 search-box-button')]").click()

# text()
driver.find_element(By.XPATH, "//button[text()='Search']").click()