from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("https://www.opencart.com/index.php?route=account/register")

driver.maximize_window()

# country_ele = driver.find_element(By.XPATH, "//select[@id='input-country']")
# country = Select(country_ele)

# OR

country = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))

# select option from dropdown

# country.select_by_visible_text("India")
# country.select_by_value("4") # America
# country.select_by_index(13) # Australia

# Capture all the options & Print it

# alloptions = country.options
# print(len(alloptions))
#
# for option in alloptions:
#     print(option.text)

# Select option from dropdown without using built-in function

# for option in alloptions:
#     if option.text == "India":
#         option.click()
#         break

# Actions without using Select class

all_options = driver.find_elements(By.XPATH, "//*[@id='input-country']/option")
print(len(all_options))

for opt in all_options:
    print(opt.text)