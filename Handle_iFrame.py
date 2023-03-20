from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.maximize_window()

driver.switch_to.frame("packageListFrame") # name of iFrame has to be passed
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()

# Note: driver can't navigate from 1 frame to the other frame.
# Navigation -> Frame1 to Page to Frame2 to Page to Frame3 etc.....
# Switching occurs only b/w page to frame and viceversa. It can't be switched from one frame to the other.

driver.switch_to.default_content() # this 'll navigate to main page.
driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "WebDriver").click()

driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]/a").click()
