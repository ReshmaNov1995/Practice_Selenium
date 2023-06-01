from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

driver.maximize_window()

button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

act =  ActionChains(driver)
act.context_click(button).perform()

driver.find_element(By.XPATH, "//li[@class='context-menu-item context-menu-icon context-menu-icon-edit']").click()

driver.switch_to.alert.accept()
