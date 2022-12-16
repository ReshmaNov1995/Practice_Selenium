from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demo.nopcommerce.com/")

# find_element - returns single element
# Locator matching single web element
# element1 = driver.find_element(By.ID, "small-searchterms")
# element1.send_keys("laptop")

# Locator matching multiple web element
# element2 = driver.find_element(By.XPATH, "//div[@class='footer']//a")
# print(element2.text)

# find_elements -  returns multiple element (It 'll return the list of elements)
# Locator matching single web element
# element1 = driver.find_elements(By.ID, "small-searchterms")
# print(len(element1))
# element1[0].send_keys("laptop")

# Locator matching multiple web element
element1 = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(len(element1))
print(element1[5].text)

for i in element1:
    print(i.text)