from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Declaring Explicit wait
# explicitwait = WebDriverWait(driver, 10,)
# ignored_exceptions= [Exception] this 'll handle the Exceptions caused by the utilisation part.
# poll_frequency=2 this will poll DOM for every 2 seconds. poll->find.
# This should be lesser than timeout time. 10 seconds will split into 2(5).
explicitwait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions= [Exception])

driver.get("https://www.google.com/")

driver.maximize_window()

searchbox = driver.find_element(By.XPATH, "//input[@class='gLFyf']")
searchbox.send_keys("selenium")
searchbox.submit()

# Utilising Explicit wait
searchelement = explicitwait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
searchelement.click()
# driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()