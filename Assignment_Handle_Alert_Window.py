from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

# Alert Actions
driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()

alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()

# Window Actions
searchbox = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("selenium")
searchicon = driver.find_element(By.CLASS_NAME, "wikipedia-search-button").click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='Wikipedia1_wikipedia-search-results-header']"),"Search results"))

searchresult = driver.find_elements(By.XPATH, "//div[@id='Wikipedia1_wikipedia-search-results']/div/a")

current_window = driver.current_window_handle

# Click all the search list
for i in searchresult:
    print(i.text)
    i.click()

# Get all the window handles
mulwindow = driver.window_handles

for j in mulwindow:
    driver.switch_to.window(j)
    print(driver.title) # Capture the title

# Switching to the first window
driver.switch_to.window(current_window)

# Switching to the Frame
driver.switch_to.frame("frame-one1434677811")

driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Reshma")

driver.quit()