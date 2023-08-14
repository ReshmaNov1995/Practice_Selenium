from selenium import webdriver
from selenium.webdriver.common.by import By
import os


location = os.getcwd() # getcurrentworkingdirectory

def chrome_setup():
    # from webdriver_manager.chrome import ChromeDriverManager
    # from selenium.webdriver.chrome.service import Service
    # serv_obj = Service(ChromeDriverManager().install())

    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    from selenium.webdriver.edge.service import Service
    serv_obj = Service(EdgeChromiumDriverManager().install())

    # download file in desired location
    # chrome_option = webdriver.ChromeOptions()
    edge_option = webdriver.EdgeOptions()
    # preferences = {"download.default_directory": "D:\\Resh\\"} # key is default, location can set as required.
    preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True} # This plugin key will automatically download PDF.

    # chrome_option.add_experimental_option("detach", True)
    # chrome_option.add_experimental_option("prefs", preferences)

    edge_option.add_experimental_option("detach", True)
    edge_option.add_experimental_option("prefs", preferences)  # prefs is default

    driver = webdriver.Edge(service=serv_obj, options=edge_option)

    return driver


driver = chrome_setup()

driver.get("https://unec.edu.az/application/uploads/2014/12/pdf-sample.pdf")

driver.maximize_window()

