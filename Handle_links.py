from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options= chrome_option)

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()

# Clicking Link

# driver.find_element(By.LINK_TEXT, "Digital downloads").click()

# Finding total no.of.links

# totallink = driver.find_elements(By.TAG_NAME, "a")
# print(len(totallink))

# OR

links = driver.find_elements(By.XPATH, "//a")
print(len(links))

# Print all link names
for i in links:
    print(i.text)
