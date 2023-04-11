import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

link="http://62.171.183.83:9096/QuaLISWeb/#/login"
user_name="r1"
password="123"

@pytest.mark.parametrize("pass1,pass2,pass3",[(link,user_name,password),(link,user_name,password),(link,user_name,password)])
@allure.severity(allure.severity_level.BLOCKER)
def test_lims_login(pass1,pass2,pass3):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)
    driver.maximize_window()
    driver.get(pass1)
    driver.find_element(By.XPATH, "//*[@name='sloginid']").send_keys(pass2)
    driver.find_element(By.XPATH, "//*[@name='spassword']").send_keys(pass3)
    WebDriverWait(driver, 40, ignored_exceptions=[Exception]).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text()='Administrator']")))
    driver.find_element(By.XPATH, "//*[text()='Login']").click()

    allure.attach(driver.get_screenshot_as_png(), name = "RK", attachment_type = AttachmentType.PNG)