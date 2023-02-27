from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.maximize_window()

date = "12"
month = "Jun"
year = "2021"

driver.find_element(By.XPATH, "//input[@id='dob']").click()

yer = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
yer.select_by_visible_text(year)
moth = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
moth.select_by_visible_text(month)

dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
    dte = ele.text
    if dte == date:
        ele.click()
        break

