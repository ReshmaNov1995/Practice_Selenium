from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("https://jqueryui.com/datepicker/")

driver.maximize_window()

driver.switch_to.frame(0)

# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("02/01/2023") #MM/DD/YYYY

year = "2020"
month = "April"
date = "19"

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

# Select Month & Year

# limit is unknown. so, use while loop
while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break

    else:
        # driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()  # Next arrow
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click() # Prev arrow

# Select Date

dte = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for i in dte:
    data = i.text
    # print(data)

    if data == date:
        i.click()
        break

