from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# capture cookies from the browser
cookies = driver.get_cookies()
print("Size of the cookies ", len(cookies))

# Details of all cookies
for c in cookies:
    # print(c)
    print(c.get("name"),":",c.get("value"))

# Add new cookie to the browser
driver.add_cookie({"name":"MyCookie", "value":"12345"})
cookies1 = driver.get_cookies()
print("Size of the cookies", len(cookies1))

# Delete Specific cookie
driver.delete_cookie("MyCookie")
cookies2 = driver.get_cookies()
print("Size of the cookies", len(cookies2))

# Delete all cookies
driver.delete_all_cookies()
cookies3 = driver.get_cookies()
print("Size of the cookies", len(cookies3))