import csv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# csv file starts from row value as '0'
kkk=[]
with open('E:\Myn\ddt2.csv') as cards:
   csv_reader = csv.reader(cards)
   for row, column in enumerate(csv_reader):  # enumerate - Split the row & column data. Then it has stored in row,column.
       # print(index)
       kk = []
       if row != 0:
           un = column[0]
           psd = column[1]
           kk.insert(0, un)
           kk.insert(1, psd)
           kkk.append(kk)

print(kkk)

@pytest.mark.parametrize("var1,var2", kkk)
def test_eval1(var1, var2):
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options)
    driver.get("https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjgwOTQ2NjYwLCJjYWxsc2l0ZV9pZCI6MjY5NTQ4NDUzMDcyMDk1MX0%3D")
    driver.find_element(By.XPATH,"//*[@name='email']").send_keys(var1)
    driver.find_element(By.XPATH,"//*[@name='pass']").send_keys(var2)
    WebDriverWait(driver,10,ignored_exceptions=[Exception]).until(EC.element_to_be_clickable((By.XPATH,"//*[@name='login']")))
    driver.find_element(By.XPATH,"//*[@name='login']").click()

