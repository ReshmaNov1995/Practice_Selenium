import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pageObjects.LoginPage import login
import pytest
import logging

class Test_login_0001_testcase():
    link="http://62.171.183.83:9096/QuaLISWeb/#/login"
    UN="system"
    PSD="123"
    def test_homepage(self,setup):
        self.driver=setup
        self.driver.get(self.link)
        self.driver.maximize_window()
        log = login(self.driver)
        title=log.link_title()
        # title=self.driver.title
        print(title)
        # caplog.set_level(logging.INFO)
        # logging.getLogger().info('title is captured:')
        logging.basicConfig(filename='logs/info.log',format='%(asctime)s,%(levelname)s,%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG)
        mylogger = logging.getLogger()
        mylogger.info(' About to start the tests ')

        if title=="Qualis LIMS1":
            assert True
        else:
            self.driver.save_screenshot("screenshots/homepage_error.png")
            assert False



    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.link)
        self.driver.maximize_window()
        log=login(self.driver)
        log.username(self.UN)
        log.password(self.PSD)
        log.login()
        log.logout()
        self.driver.close()







