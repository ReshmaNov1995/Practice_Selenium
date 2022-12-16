from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

driver.maximize_window()

# is_displayed(), is_enabled()
searchbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")

print(searchbox.is_displayed())
print(searchbox.is_enabled())

# is_selected()
male = driver.find_element(By.ID, "gender-male")
female = driver.find_element(By.ID, "gender-female")

female.click()

print(female.is_selected())