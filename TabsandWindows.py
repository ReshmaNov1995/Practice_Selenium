from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()

# keyaction = Keys.CONTROL+Keys.ENTER
# driver.find_element(By.LINK_TEXT, "Register").send_keys(keyaction)

# Open new tab & switch to it

driver.get("https://www.opencart.com/")
driver.switch_to.new_window("tab") # It will open new tab
driver.switch_to.new_window("window") # It will open new window
driver.get("https://www.orangehrm.com/")

