import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Excel_operations import Excel_Utility as eu

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.find_element(By.XPATH, "//button[@id='wzrk-cancel']").click()
driver.maximize_window()

# Get the data from Excel
# Whenever data is captured from the Excel file, It is always String data ype. So, If we gonna do validation then it has to be changed to float datatype.

file = "E:\\Automation\\Data\\Data.xlsx"
sheetname = "Sheet1"

rowcount = eu.getRowCount(file, sheetname)
# columncount = eu.getColumnCount(file, sheetname)

for r in range(2,rowcount+1):
    # reading data from excel
    principle = eu.readData(file, sheetname, r, 1)
    rateOfInterest = eu.readData(file, sheetname, r, 2)
    period1 = eu.readData(file, sheetname, r, 3)
    period2 = eu.readData(file, sheetname, r, 4)
    frequency = eu.readData(file, sheetname, r, 5)
    expMaturity = eu.readData(file, sheetname, r, 6)

    # Passing data to the Application
    driver.find_element(By.XPATH, "//*[@id='principal']").send_keys(principle)
    driver.find_element(By.XPATH, "//*[@id='interest']").send_keys(rateOfInterest)
    driver.find_element(By.XPATH, "//*[@id='tenure']").send_keys(period1)
    periodDropdown = Select(driver.find_element(By.XPATH, "//Select[@id='tenurePeriod']"))
    periodDropdown.select_by_visible_text(period2)
    frequencyDropdown = Select(driver.find_element(By.XPATH, "//Select[@id='frequency']"))
    frequencyDropdown.select_by_visible_text(frequency)
    calculate_button = driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()

    actualMaturity = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    # Validation
    if float(expMaturity) == float(actualMaturity):
        print("Test passed")
        eu.writeData(file, sheetname, r, 8, "Pass")
        eu.fillGreencolor(file, sheetname, r, 8)

    else:
        print("Test Failed")
        eu.writeData(file, sheetname, r, 8, "Fail")
        eu.fillRedcolor(file, sheetname, r, 8)
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()
