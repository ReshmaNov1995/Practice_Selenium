from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.maximize_window()

driver.get("https://demo.wpjobboard.net/wp-admin/admin.php?page=wpjb-application")

driver.find_element(By.XPATH, "//input[@id='wp-submit']").click()

names = driver.find_elements(By.XPATH, "//*[@id='the-list']/tr/td[2]/strong/a")

checkbox = driver.find_elements(By.XPATH, "//*[@id='the-list']/tr/th/input")

def method(arg1, ratings):
    for i in names:
        a = i.text
        # print(a)

        if a == arg1:

            for j in range(1, ratings + 1):
                print(j)
                driver.find_element(By.XPATH, "//*[@id='the-list']//tr[3]//*[@data-value='" + str(j) + "']").click()

method("Carl Mason", 3)
