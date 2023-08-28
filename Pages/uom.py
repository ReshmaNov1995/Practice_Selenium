from POM import POM_loginpage

from configparser import ConfigParser

config = ConfigParser()
config.read("E:\\Automation\\Practice_Selenium\\POM\\POM_locator.ini")


def add_uom():
    username = POM_loginpage.xpath_username
    userini = config.get("testdata", "user")
    print(userini)
    print(username)


add_uom()