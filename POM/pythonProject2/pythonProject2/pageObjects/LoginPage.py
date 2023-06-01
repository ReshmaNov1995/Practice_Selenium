from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
class login():
    un_xpath="//*[@id='sloginid']"
    psd_xpath="//*[@id='spassword']"
    role_xpath="//*[text()='QuaLIS Admin']"
    login_xpath="//*[text()='Login']"
    logout_xpath1 = "//*[@class='no-arrow nav-item dropdown']/child::a"
    logout_xpath2="//*[@class='dropdown-menu show dropdown-menu-right']/child::a[2]"

    # LOGGER = logging.getLogger(__name__)

    def __init__(self,driver):
        self.driver=driver


    # def debug_log(self):
    #     logging.basicConfig(filename='logs/debug.log',format='%(asctime)s,%(levelname)s,%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG)
    #     logging.debug("This debug log")
    #
    # def info_log(self):
    #     logging.basicConfig(filename='logs/info.log',format='%(asctime)s,%(levelname)s,%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG)
    #     logging.info("This info log")
    #
    #
    # def warn_log(self):
    #     logging.basicConfig(filename='logs/warn.log',format='%(asctime)s,%(levelname)s,%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG)
    #     logging.warning("This warning log")
    #     # logging.error("This error log")
    #     # logging.critical("This critical log")

    def username(self,UN):
        self.driver.find_element(By.XPATH,self.un_xpath).clear()
        self.driver.find_element(By.XPATH, self.un_xpath).send_keys(UN)
        self.warn_log()

    def password(self,PSD):
        self.driver.find_element(By.XPATH,self.psd_xpath).clear()
        self.driver.find_element(By.XPATH, self.psd_xpath).send_keys(PSD)

    def login(self):
        WebDriverWait(self.driver, 10, poll_frequency=2, ignored_exceptions=[Exception]).until(EC.visibility_of_element_located((By.XPATH, self.role_xpath)))
        self.driver.find_element(By.XPATH,self.login_xpath).click()

    def logout(self):
        WebDriverWait(self.driver, 30, poll_frequency=2, ignored_exceptions=[Exception]).until(
            EC.visibility_of_element_located((By.XPATH, self.logout_xpath1)))
        self.driver.find_element(By.XPATH, self.logout_xpath1).click()
        self.driver.find_element(By.XPATH, self.logout_xpath2).click()

    def link_title(self):
        title = self.driver.title
        return title







