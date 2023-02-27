import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT, "OrangeHRM").click()

# print(driver.current_window_handle)

windowIDs = driver.window_handles # To get the window id of all the browser window

# Approach - 1: If there are only 2 windows

# parentwindowid = windowIDs[0]
# childwindowid = windowIDs[1]
#
# print(parentwindowid)
# print(childwindowid)
#
# driver.switch_to.window(childwindowid) # switch to the corresponding window
# print(driver.title)
#
# driver.switch_to.window(parentwindowid)
# print(driver.title)

# Approach - 2: If we have multiple windows

# for windowid in windowIDs:
#     driver.switch_to.window(windowid)
#     print(driver.title)

# Approach - 3: To work on particular window

for windowid in windowIDs:
    driver.switch_to.window(windowid)
    if driver.title == "OrangeHRM":
        driver.close()
