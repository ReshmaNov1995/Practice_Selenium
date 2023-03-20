from selenium import webdriver
from selenium.webdriver.common.by import By
import os


location = os.getcwd() # getcurrentworkingdirectory

def chrome_setup():
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service(ChromeDriverManager().install())

    # download file in desired location
    chrome_option = webdriver.ChromeOptions()
    preferences = {"download.default_directory": "D:\\Resh\\"} # key is default, location can set as required.
    # preferences = {"download.default_directory": location}


    chrome_option.add_experimental_option("detach", True)
    chrome_option.add_experimental_option("prefs", preferences)  # prefs is default

    driver = webdriver.Chrome(service=serv_obj, options=chrome_option)

    return driver


driver = chrome_setup()

driver.get("http://xcal1.vodafone.co.uk/")

driver.maximize_window()

driver.execute_script("window.scrollBy(0,200)", "")

driver.find_element(By.XPATH, "/html/body/table/tbody/tr[17]/td/a[1]").click()


