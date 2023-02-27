from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.maximize_window()

driver.find_element(By.XPATH, "//div[@id='content']/div/ul/li[3]/button").click()

alert_window = driver.switch_to.alert

print(alert_window.text)

alert_window.send_keys("Hello Reshma")

alert_window.accept()

# alert_window.dismiss()