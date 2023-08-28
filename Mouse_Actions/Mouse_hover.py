import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

chrome_option = webdriver.EdgeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(EdgeChromiumDriverManager().install()), options = chrome_option)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()

time.sleep(3)

driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")

driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")

driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()

time.sleep(3)

admin = driver.find_element(By.XPATH, "//li[@class='oxd-main-menu-item-wrapper']")


# Mouse hover
act = ActionChains(driver)
time.sleep(3)
act.move_to_element(admin).perform()