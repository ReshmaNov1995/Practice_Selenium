# How many employees
# Enabled & Disabled Employee count
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()

time.sleep(3)

driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")

driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")

driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()

time.sleep(3)

# Admin-->User Management-->Users

driver.find_element(By.XPATH, "//li[@class='oxd-main-menu-item-wrapper']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//li[@class='oxd-topbar-body-nav-tab --parent --visited']").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Users").click()

# How many employees

time.sleep(3)
rows = len(driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']/div"))
print(rows)

# Enabled & Disabled Employee count

count = 0
for i in range(1, rows+1):
    # status = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div["+str(i)+"]/div/div[5]/div").text
    status = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div/div/div["+str(i)+"]").text
    # print(status)

    if status == "Disabled":
        count = +1

print("Total no.of.users ",rows)
print("Total no.of.Disabled users ", count)
print("Total no.of.Enabled users ", rows-count)
