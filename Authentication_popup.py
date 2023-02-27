from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

# driver.get("https://the-internet.herokuapp.com/basic_auth")

# Here we are injecting the username & password through the url.

driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")

driver.maximize_window()



