
from configparser import ConfigParser

config = ConfigParser()

# Specify the ini file path below
config.read("E:\\Automation\\Practice_Selenium\\POM\\POM_locator.ini")

print(config.get("login credentials", "un"))
