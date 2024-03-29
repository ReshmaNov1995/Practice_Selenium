import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

link="http://62.171.183.83:9096/QuaLISWeb/#/login"
user_name="r1"
password="123"

@pytest.mark.parametrize("pass1,pass2,pass3",[(link,user_name,password),(link,user_name,password)]) # based on set of arguments[(args)], it will run.
def test_lims_login(pass1,pass2,pass3):
    chrome_option = webdriver.EdgeOptions()
    chrome_option.add_experimental_option("detach", True)
    driver = webdriver.Edge(service = Service(EdgeChromiumDriverManager().install()), options = chrome_option)
    driver.maximize_window()
    driver.get(pass1)
    driver.find_element(By.XPATH, "//*[@name='sloginid']").send_keys(pass2)
    driver.find_element(By.XPATH, "//*[@name='spassword']").send_keys(pass3)
    WebDriverWait(driver, 40, ignored_exceptions=[Exception]).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text()='Administrator']")))
    driver.find_element(By.XPATH, "//*[text()='Login']").click()


#xdist running paralelly pip install pytest-xdist
#pytest -v -s -n 3 PyTest/test_Parameterize.py