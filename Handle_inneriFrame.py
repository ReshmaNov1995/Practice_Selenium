from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("https://demo.automationtesting.in/Frames.html")

driver.maximize_window()

driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()

outerframe = driver.find_element(By.XPATH, "//*[@id='Multiple']/iframe")
driver.switch_to.frame(outerframe)

innerframe = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

textfield = driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("Welcome")

# Navigate from innerframe to parentframe
driver.switch_to.parent_frame()
