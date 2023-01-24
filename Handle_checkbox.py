import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=chrome_option)

driver.get("https://itera-qa.azurewebsites.net/home/automation")

driver.maximize_window()

# specific checkbox
# driver.find_element(By.XPATH, "//input[@id='monday']").click()

checkboxes = driver.find_elements(By.XPATH, "(//input[@type='checkbox' and contains(@id,'day')])")

# All Checkboxes
# Approach - 1:
for i in checkboxes:
    i.click()

# Approach - 2:
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# Specifically multiple checkboxes as choice

# for checkbox in checkboxes: # weekdays - xpath of the elements
#     weekday = checkbox.get_attribute('id') # from each xpath element retrieving particular attribute's value
#     print(weekday)
#     if weekday=='monday' or weekday=='saturday': # compare the retrieved value with required data
#         time.sleep(5)
#         checkbox.click()

# Select last 2 checkbox
# starting index = total(7)-required(2)---> 5

# for i in range(len(checkboxes)-2, len(checkboxes)): # range(5,7) --> 6,7
#     checkboxes[i].click()

# Select first 2 checkbox

# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

# Clearing all the checkboxes

time.sleep(5)
for i in checkboxes:
    if i.is_selected():
        i.click()