import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# implicit wait - It has to be written while starting the script. Because, this will handle the synchronization problem for every line of code.
driver.implicitly_wait(10)

driver.get("https://www.google.com/")

driver.maximize_window()

searchbox = driver.find_element(By.XPATH, "//input[@class='gLFyf']")
searchbox.send_keys("selenium")
searchbox.submit()

#time -  It ll stop the program execution for the mentioned time period.
# time.sleep(5)
driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()
