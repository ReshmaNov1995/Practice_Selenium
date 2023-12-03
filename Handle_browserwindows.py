import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

edge_options=webdriver.EdgeOptions()
edge_options.add_experimental_option("detach",True)
edge_options.headless = True

driver=webdriver.Edge(service = Service(EdgeChromiumDriverManager().install()), options=edge_options)

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT, "OrangeHRM").click()

print(driver.current_window_handle)

windowIDs = driver.window_handles # To get the window id of all the browser window
print(windowIDs)

# Approach - 1: If there are only 2 windows

parentwindowid = windowIDs[0]
childwindowid = windowIDs[1]

print(parentwindowid)
print(childwindowid)

driver.switch_to.window(childwindowid) # switch to the corresponding window
print(driver.title)

driver.switch_to.window(parentwindowid)
print(driver.title)

# Approach - 2: If we have multiple windows

for windowid in windowIDs:
    driver.switch_to.window(windowid)
    print(driver.title)

# Approach - 3: To work on particular window

for windowid in windowIDs:
    driver.switch_to.window(windowid)
    if driver.title == "OrangeHRM":
        driver.close()
