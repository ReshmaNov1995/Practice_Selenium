from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome()

service_obj = Service("E:\Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.get("https://www.snapdeal.com")
driver.get("https://www.amazon.com")

# driver.back()
# driver.forward()
# driver.refresh()