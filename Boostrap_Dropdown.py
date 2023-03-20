import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

time.sleep(3)
country_dropdown = driver.find_element(By.XPATH, "//*[@id='select2-billing_country-container']")
driver.execute_script("arguments[0].scrollIntoView();", country_dropdown)
country_dropdown.click()

countrylist = driver.find_elements(By.XPATH, "//ul[@class='select2-results__options']/li")
print(len(countrylist))

for country in countrylist:
    if country.text == "American Samoa":
        country.click()
        break
