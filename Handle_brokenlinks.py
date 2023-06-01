import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_option)

driver.get("http://www.deadlinkcity.com/")

driver.maximize_window()

# "requests" to be installed, it's a pre-requesite

alllinks = driver.find_elements(By.XPATH, "//a")
brokenLinkCount = 0
validLinkCount = 0

for link in alllinks:
    url = link.get_attribute("href")
    try:
        resp = requests.head(url)
        print(resp)
    except:
        pass
    if resp.status_code>=400:
        print(url, " is a Broken link")
        brokenLinkCount+=1

    else:
        print(url, " is a Valid link")
        validLinkCount+=1

print("Total no.of.Broken link is ", brokenLinkCount)
print("Total Valid link", validLinkCount)