import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://admin-demo.nopcommerce.com/login")

# Email box
email = driver.find_element(By.XPATH, "//input[@id='Email']")
email.clear()
email.send_keys("abc@gmail.com")

# text - will return the inner text of the element.
# ex: <input id ='123' class = 'name'> Email: </input> Here Email: is inner text
print("result of text:", email.text)

# get attribute - will return the value of any element.
print("result of get_attribute():", email.get_attribute('value')) # value is a attribute

time.sleep(5)

# Login button
login = driver.find_element(By.XPATH, "//button[@class='button-1 login-button']")

print("result of text:", login.text)
print("result of get_attribute():", login.get_attribute('type'))