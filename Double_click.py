import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")

driver.maximize_window()

frame = driver.find_element(By.XPATH, "//iframe[@id='iframeResult']")
driver.switch_to.frame(frame)

# time.sleep(3)
button = driver.find_element(By.XPATH, "//button[text()='Copy Text']")

act = ActionChains(driver)
act.double_click(button).perform()
