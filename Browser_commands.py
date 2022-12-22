import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_option)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()

time.sleep(5)

orangehrmlink = driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc")
orangehrmlink.click()

time.sleep(5)

# driver.close()

# driver.quit()