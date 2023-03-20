import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()

# scroll down by pixel
# driver.execute_script("window.scrollBy(0,3000)", "") # scroll down
# value = driver.execute_script("return window.pageYOffset")
# print("No.of.Pixels moved ", value)

# scroll down till element is visible
# flag = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# value = driver.execute_script("return window.pageYOffset")
# print("No.of.Pixels moved ", value)

# scroll down till element is visible - Method-2
# flag.location_once_scrolled_into_view

# scroll till end of the page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
# value = driver.execute_script("return window.pageYOffset")
# print("No.of.Pixels moved ", value) # 5942.39990234375

# scroll up page by pixel
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")

# Horizontall scroll to the page
# driver.execute_script("window.scrollBy(document.body.scrollHeight, 0)")

# scroll up the page by Keys
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + Keys.HOME)

# scroll down the page by keys
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + Keys.END)

