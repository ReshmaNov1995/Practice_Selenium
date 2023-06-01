from configparser import ConfigParser

config = ConfigParser()

config.read("E:\Automation\Practice_Selenium\Configuration\samplefile.ini")

link = config.get("LoginCredentials", "link") # section name, Key name
print(link)