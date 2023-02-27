# Fetch the Username of userrole ESS. Print both Username, userrole

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

driver.find_element(By.XPATH, "//li[@class='oxd-main-menu-item-wrapper']").click()

time.sleep(3)

driver.find_element(By.XPATH, "//li[@class='oxd-topbar-body-nav-tab --parent --visited']").click()

time.sleep(3)

driver.find_element(By.LINK_TEXT, "Users").click()

time.sleep(3)

rows = len(driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']/div"))
print(rows)

for r in range(1, rows+1):
    userRole = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div["+str(r)+"]/div/div[3]/div").text
    # print(userRole)
    if userRole == "ESS":
        user = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div["+str(r)+"]/div/div[2]/div").text
        print("For the UserRole "+userRole+" User name is "+user)