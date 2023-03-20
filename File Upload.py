from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("https://www.foundit.in/")
driver.maximize_window()

driver.find_element(By.XPATH, "//div[@class='heroSection-buttonContainer_secondaryBtn__text']").click()
driver.find_element(By.XPATH, "//input[@id='file-upload']").send_keys("C:\\Users\\Reshma S\\Downloads\\Export - 2023-03-17T191519.716.pdf")